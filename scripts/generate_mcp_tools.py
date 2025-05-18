import json
import re
from pathlib import Path


def method_to_func_name(method: str) -> str:
    return method.lower()


def generate_interface(method: str, params: list) -> str:
    """Generate an abstract method declaration for the interface."""
    # Count the number of parameters
    param_count = len(params) if params else 0

    # Generate the parameter list
    if param_count > 0:
        param_list = ", ".join([f"param{i}: str" for i in range(param_count)])
        return f"    @abstractmethod\n    async def {method_to_func_name(method)}(self, {param_list}) -> str: ...\n"
    else:
        return (
            f"    @abstractmethod\n    async def {method_to_func_name(method)}(self) -> str: ...\n"
        )


def generate_client_router(method: str, params: list) -> str:
    """Generate a client router function for the method."""
    # Count the number of parameters
    param_count = len(params) if params else 0

    # Generate the parameter list
    if param_count > 0:
        param_list = ", ".join(["chain"] + [f"param{i}" for i in range(param_count)])
        pass_params = ", ".join([f"param{i}" for i in range(param_count)])
        return f"async def {method_to_func_name(method)}({param_list}):\n    return await _adapter(chain).{method_to_func_name(method)}({pass_params})\n\n"
    else:
        return f"async def {method_to_func_name(method)}(chain):\n    return await _adapter(chain).{method_to_func_name(method)}()\n\n"


def generate_tool(method: str, params: list) -> str:
    """Generate a tool function for the method."""
    func_name = method_to_func_name(method)

    # Count the number of parameters
    param_count = len(params) if params else 0

    # Generate the parameter list
    if param_count > 0:
        param_list = ", ".join(["chain: str"] + [f"param{i}: str" for i in range(param_count)])
        arg_list = ", ".join(["chain.lower()"] + [f"param{i}" for i in range(param_count)])
    else:
        param_list = "chain: str"
        arg_list = "chain.lower()"

    return f"""@mcp.tool(
    name="{func_name}",
    description="Auto-generated tool for {method}",
    annotations={{"title": "{method}", "readOnlyHint": True}},
)
async def {func_name}({param_list}) -> CallToolResult:
    try:
        return _ok(await client.{func_name}({arg_list}))
    except Exception as e:
        return _err(str(e))

"""


def generate_adapter_method(method: str, params: list) -> str:
    """Generate an adapter method implementation."""
    func_name = method_to_func_name(method)

    # Count the number of parameters
    param_count = len(params) if params else 0

    # Generate the parameter list and call parameters
    if param_count > 0:
        param_list = ", ".join([f"param{i}" for i in range(param_count)])
        call_params = ", ".join([f"param{i}" for i in range(param_count)])
        return f'    async def {func_name}(self, {param_list}) -> str:\n        return await self.rpc_client.post("{method}", [{call_params}], self.rpc_url)\n\n'
    else:
        return f'    async def {func_name}(self) -> str:\n        return await self.rpc_client.post("{method}", [], self.rpc_url)\n\n'


def generate_adapter_file(methods_info, blockchain: str) -> str:
    header = f'''
"""
Auto-generated adapter class for {blockchain}-compatible blockchain.
"""

from common.interfaces import RpcClient
from common.rpc import HttpxRpcClient
from servers.{blockchain}.common.interfaces import BlockchainAdapter


class {blockchain.capitalize()}Adapter(BlockchainAdapter):
    def __init__(self, rpc_url: str, rpc_client: RpcClient = None):
        self.rpc_url = rpc_url
        self.rpc_client = rpc_client or HttpxRpcClient()

'''
    body = ""
    for method, params in methods_info:
        body += generate_adapter_method(method, params)
    return header + body


def extract_methods_from_text(openapi_text: str):
    pattern = r'"method":\s*\{[^}]*"default":\s*"([^"]+)"[^}]*\}.*?"params":\s*\{[^}]*"default":\s*(\[[^\]]*\])'
    matches = re.findall(pattern, openapi_text, re.DOTALL)
    methods_info = []
    for method, params_str in matches:
        try:
            cleaned = params_str.replace("\n", "").replace('\\"', '"')
            params = eval(cleaned, {"__builtins__": {}}, {})
            methods_info.append((method, params))
        except Exception:
            continue
    return methods_info


def extract_methods_from_json_files(file_paths):
    """Extract method information from multiple JSON files or a combined text file."""
    methods_info = []

    # Convert to list if it's not
    if not isinstance(file_paths, list):
        file_paths = [file_paths]

    for file_path in file_paths:
        if not Path(file_path).exists():
            print(f"Warning: File does not exist: {file_path}")
            continue

        with open(file_path) as f:
            content = f.read()

        # Check if this is a combined file with multiple JSON objects
        if "================================================" in content:
            # Split the file by the delimiter
            json_parts = re.split(r"={10,}\nFILE:.*\n={10,}\n", content)

            for part in json_parts:
                if not part.strip():
                    continue

                try:
                    # Try to parse each part as JSON
                    data = json.loads(part)
                    part_methods = extract_methods_from_json(data)
                    if part_methods:
                        methods_info.extend(part_methods)
                    else:
                        # If no methods found, try regex approach
                        methods_info.extend(extract_methods_from_text(part))
                except json.JSONDecodeError:
                    # If it fails, use regex approach
                    methods_info.extend(extract_methods_from_text(part))
        else:
            # Try to parse as a single JSON file
            try:
                data = json.loads(content)
                json_methods = extract_methods_from_json(data)
                if json_methods:
                    methods_info.extend(json_methods)
                else:
                    # If no methods found, try regex approach
                    methods_info.extend(extract_methods_from_text(content))
            except json.JSONDecodeError:
                # If it fails, use regex approach
                methods_info.extend(extract_methods_from_text(content))

    # Debug print
    print(f"Found {len(methods_info)} methods:")
    for method, params in methods_info:
        print(f"  - {method}: {len(params)} parameters")

    return methods_info


def extract_methods_from_json(data):
    """Extract method information from a parsed JSON object."""
    methods_info = []

    # Navigate through paths to find methods and parameters
    if "paths" in data:
        for path, path_info in data["paths"].items():
            for method_type, operation in path_info.items():
                if "requestBody" in operation and "content" in operation["requestBody"]:
                    content = operation["requestBody"]["content"]
                    if "application/json" in content and "schema" in content["application/json"]:
                        schema = content["application/json"]["schema"]
                        if "properties" in schema:
                            props = schema["properties"]
                            if "method" in props and "default" in props["method"]:
                                method_name = props["method"]["default"]

                                if "params" in props and "default" in props["params"]:
                                    params = props["params"]["default"]
                                    methods_info.append((method_name, params))

    return methods_info


def generate_all(openapi_file: str, out_dir: str, blockchain: str):
    openapi_path = Path(openapi_file)

    if openapi_path.is_dir():
        files = list(openapi_path.glob("**/*.json")) + list(openapi_path.glob("**/*.txt"))
        methods_info = extract_methods_from_json_files(files)
    else:
        with open(openapi_file) as f:
            raw_txt = f.read()
        try:
            data = json.loads(raw_txt)
            methods_info = extract_methods_from_json(data)
        except json.JSONDecodeError:
            methods_info = extract_methods_from_text(raw_txt)

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    Path(f"{out_dir}/__init__.py").write_text("")

    if not methods_info:
        print(f"No methods found in {openapi_file}")
        return

    Path(f"{out_dir}/interfaces.py").write_text('''"""
Auto-generated abstract methods based on JSON-RPC OpenAPI specification.
"""

from abc import ABC, abstractmethod


class BlockchainAdapter(ABC):
''')
    Path(f"{out_dir}/client.py").write_text(f'''"""
Auto-generated client router methods for MCP.
"""

from servers.{blockchain}.common.adapter_registry import registry


def _adapter(chain: str):
    ad = registry.get(chain)
    if not ad:
        raise ValueError(f"Unsupported blockchain: {{chain}}")
    return ad

''')
    Path(f"{out_dir}/json_rpc_methods.py").write_text(f'''"""
Auto-generated MCP tools for JSON-RPC methods.
"""

from mcp.types import CallToolResult
from common.utils import _err, _ok
import servers.{blockchain}.common.client as client
from servers.{blockchain}.server import mcp

''')

    for method, params in methods_info:
        with open(f"{out_dir}/interfaces.py", "a") as f:
            f.write(generate_interface(method, params))
        with open(f"{out_dir}/client.py", "a") as f:
            f.write(generate_client_router(method, params))
        with open(f"{out_dir}/json_rpc_methods.py", "a") as f:
            f.write(generate_tool(method, params))

    adapter_code = generate_adapter_file(methods_info, blockchain)
    Path(f"{out_dir}/{blockchain}.py").write_text(adapter_code)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print(
            "Usage: uv run scripts/generate_mcp_tools.py <openapi_path> <output_dir> <blockchain_name>"
        )
        print("  openapi_path: Path to OpenAPI file or directory containing JSON files")
        print("  output_dir: Directory to output generated files")
        print("  blockchain_name: Name of the blockchain (e.g., ethereum)")
        sys.exit(1)

    openapi_path = sys.argv[1]
    output_dir = sys.argv[2]
    blockchain_name = sys.argv[3]
    generate_all(openapi_path, output_dir, blockchain_name)
