#!/usr/bin/python3
'''python script that takes an email and
sends a post requst to the passed url'''


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    req = urllib.request.Request(url, email=email)
    with urllib.request.urlopen(req) as res:
        response_page = res.read()
        print(response_page.decode("utf-8"))
