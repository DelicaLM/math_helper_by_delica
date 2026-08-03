from .new_python_funcs import *
from importlib.metadata import version, PackageNotFoundError

__version__ = "unknown"
try:
    __version__ = version("new_python_package")
except PackageNotFoundError:
    pass

__all__ = ["new_python_funcs"]
