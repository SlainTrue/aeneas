#!/usr/bin/env python
# coding=utf-8

"""
Compile the Python C Extension for computing the MFCCs.

.. versionadded:: 1.1.0
"""

import os
import sys

from distutils.core import setup, Extension
from numpy.distutils import misc_util

__author__ = "Alberto Pettarin"
__copyright__ = """
    Copyright 2012-2013, Alberto Pettarin (www.albertopettarin.it)
    Copyright 2013-2015, ReadBeyond Srl   (www.readbeyond.it)
    Copyright 2015,      Alberto Pettarin (www.albertopettarin.it)
    """
__license__ = "GNU AGPL v3"
__version__ = "1.2.0"
__email__ = "aeneas@readbeyond.it"
__status__ = "Production"

for compiled in ["cmfcc.so", "cmfcc.dylib", "cmfcc.dll"]:
    if os.path.exists(compiled):
        try:
            os.remove(compiled)
            print "[INFO] Removed file %s\n" % compiled
        except:
            pass

CMODULE = Extension("cmfcc", sources=["cmfcc.c"])

setup(
    name="cmfcc",
    version="1.1.1",
    description="""
    Python C Extension for computing the MFCCs as fast as your bare metal allows.
    """,
    ext_modules=[CMODULE],
    include_dirs=misc_util.get_numpy_include_dirs()
)

print "\n[INFO] Module cmfcc successfully compiled\n"
sys.exit(0)


