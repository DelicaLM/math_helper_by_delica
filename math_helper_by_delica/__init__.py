from .math_helper_funcs import *
from importlib.metadata import version, PackageNotFoundError

__version__ = "unknown"
try:
    __version__ = version("math_helper_by_delica")
except PackageNotFoundError:
    pass

__all__ = ["math_helper_funcs.py"]
