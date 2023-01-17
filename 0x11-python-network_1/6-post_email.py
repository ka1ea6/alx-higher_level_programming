#!/usr/bin/python3
'''Python script that takes in a URL and an email
address sends a POST request to the passed URL'''

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    res = requests.get(url, data={"email": email})

    print(res.text)
