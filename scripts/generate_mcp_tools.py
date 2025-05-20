import json
import re
from pathlib import Path


def method_to_func_name(method: str) -> str:
    return method.lower()


def generate_interface(method_info):
    """Generate an abstract method declaration for the interface."""
    method_name = method_info["name"]
    params = method_info["params"]

    param_count = len(params)
    if param_count > 0:
        param_list = ", ".join([f"{param['name']}: str" for param in params])
        return f"    @abstractmethod\n    async def {method_to_func_name(method_name)}(self, {param_list}) -> str: ...\n"
    else:
        return f"    @abstractmethod\n    async def {method_to_func_name(method_name)}(self) -> str: ...\n"


def generate_client_router(method_info):
    """Generate a client router function for the method."""
    method_name = method_info["name"]
    params = method_info["params"]

    param_count = len(params)
    if param_count > 0:
        param_list = ", ".join(["chain"] + [param["name"] for param in params])
        pass_params = ", ".join([param["name"] for param in params])
        return f"async def {method_to_func_name(method_name)}({param_list}):\n    return await _adapter(chain).{method_to_func_name(method_name)}({pass_params})\n\n"
    else:
        return f"async def {method_to_func_name(method_name)}(chain):\n    return await _adapter(chain).{method_to_func_name(method_name)}()\n\n"


def generate_tool(method_info):
    """Generate a tool function for the method."""
    method_name = method_info["name"]
    params = method_info["params"]
    summary = method_info["summary"]
    description = method_info["description"]
    returns = method_info["returns"]

    # Create a detailed description for the tool
    tool_description = f"Call the {method_name} JSON-RPC method"
    if summary:
        tool_description += f": {summary}"
    if description:
        tool_description += f"\n{description}"
    if returns:
        tool_description += f"\nReturns: {returns}"

    # Add parameter descriptions
    if params:
        tool_description += "\n\nParameters:"
        for param in params:
            param_desc = f"\n- {param['name']}"
            if param.get("title"):
                param_desc += f" ({param['title']})"
            if param.get("description"):
                param_desc += f": {param['description']}"
            if isinstance(param.get("value"), dict):
                inner_fields = ", ".join([f"{k}={v}" for k, v in param["value"].items()])
                param_desc += f" [Object Example: {{{inner_fields}}}]"
            elif "value" in param and param.get("value"):
                param_desc += f" [Example: {param['value']}]"
            tool_description += param_desc

    func_name = method_to_func_name(method_name)

    param_count = len(params)
    if param_count > 0:
        param_list = ", ".join(["chain: str"] + [f"{param['name']}: str" for param in params])
        arg_list = ", ".join(["chain.lower()"] + [param["name"] for param in params])
    else:
        param_list = "chain: str"
        arg_list = "chain.lower()"

    return f"""@mcp.tool(
    name="{func_name}",
    description={json.dumps(tool_description)},
    annotations={{"title": "{method_name}", "readOnlyHint": True}},
)
async def {func_name}({param_list}) -> CallToolResult:
    try:
        return _ok(await client.{func_name}({arg_list}))
    except Exception as e:
        return _err(str(e))

"""


def generate_adapter_method(method_info):
    """Generate an adapter method implementation."""
    method_name = method_info["name"]
    params = method_info["params"]

    param_count = len(params)
    if param_count > 0:
        param_list = ", ".join([param["name"] for param in params])
        call_params = ", ".join([param["name"] for param in params])
        return f'    async def {method_to_func_name(method_name)}(self, {param_list}) -> str:\n        return await self.rpc_client.post("{method_name}", [{call_params}], self.rpc_url)\n\n'
    else:
        return f'    async def {method_to_func_name(method_name)}(self) -> str:\n        return await self.rpc_client.post("{method_name}", [], self.rpc_url)\n\n'


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
    for method in methods_info:
        body += generate_adapter_method(method)
    return header + body


def extract_methods_from_text(openapi_text: str):
    """Extract method information using regex when JSON parsing fails."""
    pattern = r'"method":\s*\{[^}]*"default":\s*"([^"]+)"[^}]*\}.*?"params":\s*\{[^}]*"default":\s*(\[[^\]]*\])'
    matches = re.findall(pattern, openapi_text, re.DOTALL)
    methods_info = []
    for method, params_str in matches:
        try:
            cleaned = params_str.replace("\n", "").replace('\\"', '"')
            params = eval(cleaned, {"__builtins__": {}}, {})
            methods_info.append(
                {
                    "name": method,
                    "params": [{"name": f"param{i + 1}"} for i in range(len(params))],
                    "summary": "",
                    "description": "",
                    "returns": "",
                }
            )
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
            # This regex matches the delimiter pattern used in the example files
            json_parts = re.split(r"={10,}\nFILE:.*\n={10,}", content)

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
    for method in methods_info:
        method_name = method["name"]
        param_count = len(method["params"])
        print(f"  - {method_name}: {param_count} parameters")

    return methods_info


def extract_methods_from_json(data):
    """Extract method information from a parsed JSON object."""
    methods_info = []

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
                                params_info = []

                                if "params" in props:
                                    params_prop = props["params"]
                                    param_default = params_prop.get("default", [])

                                    # Debug info
                                    print(f"Processing method: {method_name}")
                                    print(f"Params property type: {type(params_prop)}")

                                    # Handle different ways parameters can be structured
                                    if "items" in params_prop:
                                        param_items = params_prop["items"]

                                        # Handle anyOf case
                                        if "anyOf" in param_items:
                                            default_vals = (
                                                param_default
                                                if isinstance(param_default, list)
                                                else []
                                            )
                                            for idx, item in enumerate(param_items["anyOf"]):
                                                if item.get("type") == "string":
                                                    params_info.append(
                                                        {
                                                            "name": "account",
                                                            "title": "",
                                                            "description": item.get(
                                                                "description", ""
                                                            ),
                                                            "value": item.get("default", ""),
                                                        }
                                                    )
                                                elif (
                                                    item.get("type") == "object"
                                                    and "properties" in item
                                                ):
                                                    object_example = {
                                                        k: v.get("default", "")
                                                        for k, v in item["properties"].items()
                                                    }
                                                    field_descriptions = []
                                                    for k, v in item["properties"].items():
                                                        desc = v.get("description", "")
                                                        if desc:
                                                            field_descriptions.append(
                                                                f"{k}: {desc}"
                                                            )
                                                        else:
                                                            field_descriptions.append(k)
                                                    params_info.append(
                                                        {
                                                            "name": "options",
                                                            "title": "Options object",
                                                            "description": "Options including: "
                                                            + ", ".join(field_descriptions),
                                                            "value": object_example,
                                                        }
                                                    )

                                        # Handle oneOf case
                                        elif "oneOf" in param_items:
                                            one_of = param_items["oneOf"]
                                            for idx, item in enumerate(one_of):
                                                param_name = f"param{idx + 1}"
                                                # If it's a primitive type with description, use param1
                                                if "type" in item and item["type"] in [
                                                    "string",
                                                    "integer",
                                                    "boolean",
                                                ]:
                                                    params_info.append(
                                                        {
                                                            "name": param_name,
                                                            "title": item.get("title", ""),
                                                            "description": item.get(
                                                                "description", ""
                                                            ),
                                                            "value": item.get("default", ""),
                                                        }
                                                    )
                                                # If it's an object with properties, extract parameter names
                                                elif (
                                                    item.get("type") == "object"
                                                    and "properties" in item
                                                ):
                                                    # Use the first property name as param name
                                                    keys = list(item["properties"].keys())
                                                    if keys:
                                                        obj_param_name = keys[0]
                                                        if obj_param_name in {
                                                            "from",
                                                            "to",
                                                            "class",
                                                            "global",
                                                        }:
                                                            obj_param_name += "_"
                                                        params_info.append(
                                                            {
                                                                "name": obj_param_name,
                                                                "title": item.get("title", ""),
                                                                "description": item.get(
                                                                    "description", ""
                                                                ),
                                                                "value": item.get("default", ""),
                                                            }
                                                        )
                                                    else:
                                                        params_info.append(
                                                            {
                                                                "name": param_name,
                                                                "title": item.get("title", ""),
                                                                "description": item.get(
                                                                    "description", ""
                                                                ),
                                                                "value": item.get("default", ""),
                                                            }
                                                        )
                                                else:
                                                    params_info.append(
                                                        {
                                                            "name": param_name,
                                                            "title": item.get("title", ""),
                                                            "description": item.get(
                                                                "description", ""
                                                            ),
                                                            "value": item.get("default", ""),
                                                        }
                                                    )

                                        # Direct type specification (primitive types)
                                        elif "type" in param_items:
                                            item_type = param_items["type"]
                                            if item_type in [
                                                "string",
                                                "boolean",
                                                "integer",
                                                "number",
                                            ]:
                                                params_info.append(
                                                    {
                                                        "name": "param1",
                                                        "title": param_items.get("title", ""),
                                                        "description": param_items.get(
                                                            "description", ""
                                                        ),
                                                        "value": param_items.get("default", ""),
                                                    }
                                                )
                                            # Handle direct array items with object properties
                                            elif (
                                                item_type == "object"
                                                and "properties" in param_items
                                            ):
                                                for name, info in param_items["properties"].items():
                                                    safe_name = (
                                                        name + "_"
                                                        if name in {"from", "to", "class", "global"}
                                                        else name
                                                    )
                                                    params_info.append(
                                                        {
                                                            "name": safe_name,
                                                            "title": info.get("title", ""),
                                                            "description": info.get(
                                                                "description", ""
                                                            ),
                                                            "value": info.get("default", ""),
                                                        }
                                                    )

                                    # If we found no parameters but have defaults, infer from defaults
                                    if not params_info and param_default:
                                        for idx, _ in enumerate(param_default):
                                            params_info.append(
                                                {
                                                    "name": f"param{idx + 1}",
                                                    "title": "",
                                                    "description": f"Parameter {idx + 1}",
                                                    "value": "",
                                                }
                                            )

                                    # If still no parameters found, check if we can extract from the actual default values
                                    if (
                                        not params_info
                                        and isinstance(param_default, list)
                                        and len(param_default) > 0
                                    ):
                                        for idx, default_val in enumerate(param_default):
                                            if isinstance(default_val, dict):
                                                # Extract param names from dictionary keys
                                                for key in default_val.keys():
                                                    safe_key = (
                                                        key + "_"
                                                        if key in {"from", "to", "class", "global"}
                                                        else key
                                                    )
                                                    params_info.append(
                                                        {
                                                            "name": safe_key,
                                                            "title": "",
                                                            "description": f"Parameter {safe_key}",
                                                            "value": "",
                                                        }
                                                    )
                                            else:
                                                params_info.append(
                                                    {
                                                        "name": f"param{idx + 1}",
                                                        "title": "",
                                                        "description": f"Parameter {idx + 1}",
                                                        "value": "",
                                                    }
                                                )

                                # Log a warning if no parameters were found
                                if "params" in props and not params_info:
                                    print(
                                        f"Warning: No parameters extracted for method {method_name}"
                                    )
                                    print(f"Params property: {props['params']}")

                                methods_info.append(
                                    {
                                        "name": method_name,
                                        "params": params_info,
                                        "summary": operation.get("summary", ""),
                                        "description": operation.get("description", ""),
                                        "returns": operation.get("responses", {})
                                        .get("200", {})
                                        .get("description", ""),
                                    }
                                )

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

    for method_info in methods_info:
        with open(f"{out_dir}/interfaces.py", "a") as f:
            f.write(generate_interface(method_info))
        with open(f"{out_dir}/client.py", "a") as f:
            f.write(generate_client_router(method_info))
        with open(f"{out_dir}/json_rpc_methods.py", "a") as f:
            f.write(generate_tool(method_info))

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
