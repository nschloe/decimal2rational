# -*- coding: utf-8 -*-
#
from __future__ import print_function

from . import cli
from .__about__ import __author__, __author_email__, __version__, __website__
from .main import findpoly, identify

__all__ = [
    "__version__",
    "__author__",
    "__author_email__",
    "__website__",
    "identify",
    "findpoly",
    "cli",
]

try:
    import pipdate
except ImportError:
    pass
else:
    if pipdate.needs_checking(__name__):
        print(pipdate.check(__name__, __version__), end="")
