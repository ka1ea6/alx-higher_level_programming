#!/usr/bin/python3
'''Python script that takes a leter and posts'''

if __name__ == "__main__":
    import requests
    import sys

    q = ""
    if sys.argv[1] is not None:
        q = sys.argv[1]

    res = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    res_json = res.json()
    print(f"[{res_json.get('id')}] {res_json.get('name')}")
