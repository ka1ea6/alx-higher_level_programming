#!/usr/bin/python3
'''Python script that takes in a URL, sends a request
to the URL.'''


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(res.info().get("X-Request-id"))
