#!/usr/bin/env python
# coding=utf-8

"""
Use the wrapper around ``espeak``
"""

import sys

from aeneas.espeakwrapper import ESPEAKWrapper

__author__ = "Alberto Pettarin"
__copyright__ = """
    Copyright 2012-2013, Alberto Pettarin (www.albertopettarin.it)
    Copyright 2013-2015, ReadBeyond Srl   (www.readbeyond.it)
    Copyright 2015,      Alberto Pettarin (www.albertopettarin.it)
    """
__license__ = "GNU AGPL 3"
__version__ = "1.2.0"
__email__ = "aeneas@readbeyond.it"
__status__ = "Production"

def usage():
    """ Print usage message """
    name = "aeneas.tools.espeak_wrapper"
    print ""
    print "Usage:"
    print "  $ python -m %s text language /path/to/output_file" % name
    print ""
    print "Example:"
    print "  $ python -m %s \"From fairest creatures we desire increase\" en /tmp/sonnet1.wav" % name
    print ""

def main():
    """ Entry point """
    if len(sys.argv) < 4:
        usage()
        return
    text = sys.argv[1]
    language = sys.argv[2]
    output_file_path = sys.argv[3]
    synt = ESPEAKWrapper()
    synt.synthesize(text, language, output_file_path)
    print "[INFO] Created file '%s'" % output_file_path

if __name__ == '__main__':
    main()



