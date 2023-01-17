#!/usr/bin/python3
'''Python Script to fetch from a given url
using the urllib package'''


if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    # req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        response_page = res.read()
        print("Body response:")
        print(f'\t- type: {type(response_page)}')
        print(f'\t- content: {response_page}')
        print(f'\t- utf8 content: {response_page.decode("utf-8")}')
