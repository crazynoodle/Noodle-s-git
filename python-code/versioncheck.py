#!/usr/bin/python2.7
# Filename: version_check.py

import sys, warnings

if sys.version_info[0] < 3:
    warnings.warn("Need Python 3.0 for this program to run",RuntimeWarning)
else:
    print('Proceed as normal')
