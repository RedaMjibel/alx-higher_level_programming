#!/usr/bin/python3
""" fetches a URL an prints the body of the response """


import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode("utf-8")))
    except urllib.error.URLError as e:
        print(f"Error:{e}")
