#!/usr/bin/python3
'''Python script that takes in a URL, sends a request
to the URL.'''

import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    print(res.info()['X-Request-Id'])
