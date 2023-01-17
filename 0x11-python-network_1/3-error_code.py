#!/usr/bin/python3
'''Python script that takes in a URL sends a 
request and displays the body of the response'''


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as res:
        try:
            response_page = res.read()
            print(response_page.decode('utf-8'))
        except urllib.error.HTTPError as e:
            print(f"Error Code: {e.code}")
