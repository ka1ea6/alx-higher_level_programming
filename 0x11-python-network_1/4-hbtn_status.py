#!/usr/bin/python3
'''python script to fetch from a url
using the requests package'''

if __name__ == "__main__":
    import requests
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
