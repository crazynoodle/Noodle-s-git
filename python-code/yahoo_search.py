#!/usr/bin/python2.7
# Filename: yahoo_search.py

import sys

if sys.version_info[0] != 3:
    sys.exit('This program needs Python 3.0')

import json
import urllib, urllib.parse, urllib.request, urllib.response

#Get your own APP ID at http://developer.yahoo.com/wsregapp/
YAHOO_APP_ID = '
