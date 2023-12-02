#!/usr/bin/python3
""" fetches a URL an prints the body of the response """


import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        response = requests.get("https://alx-intranet.hbtn.io/status")
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    except requests.RequestException as e:
        print(f"Error:{e}")
