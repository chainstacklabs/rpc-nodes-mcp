# chains/__init__.py
import importlib
import pkgutil

__all__ = []

for mod in pkgutil.iter_modules(__path__):  # auto-discovers direct sub-modules
    module = importlib.import_module(f"{__name__}.{mod.name}")
    globals()[mod.name] = module  # make chains.<name> importable
    __all__.append(mod.name)  # keeps tab-completion happy
