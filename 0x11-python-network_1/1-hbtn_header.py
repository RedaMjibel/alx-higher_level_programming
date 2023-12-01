#!/usr/bin/python3
""" fetches a URL an prints the X-Request-Id """


import urllib.request
import sys

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            x_request_id = response.info()
            if x_request_id:
                print(x_request_id['X-Request-Id'])
    except urllib.error.URLError as e:
        print(f"Error:{e}")
