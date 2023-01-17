#!/usr/bin/python3
'''Python script that takes in a URL
sends a request and displays the value of the
variable X-Request-Id in the response
header'''

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
