#!/usr/bin/python3
'''Python script to take github credentials and
display github id'''

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    pat = sys.argv[2]

    res = requests.get(
        f"https://api.github.com/users/{username}",
        headers={"Authorization": f"Bearer {pat}"})
    res_message = res.json().get("message")
    if res_message and res_message == "Bad credentials":
        print("None")
    else:
        print(res.json().get("id"))
