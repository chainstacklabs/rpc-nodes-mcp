# src/servers/pumpfun/tools/__init__.py
import importlib
import pkgutil

__all__ = []

# Force import all modules to ensure tool registration
for mod in pkgutil.iter_modules(__path__):
    try:
        module = importlib.import_module(f"{__name__}.{mod.name}")
        globals()[mod.name] = module
        __all__.append(mod.name)

        # Log successful import for debugging
        print(f"Successfully imported Solana tool module: {mod.name}")
    except ImportError as e:
        print(f"Failed to import Solana tool module {mod.name}: {e}")
