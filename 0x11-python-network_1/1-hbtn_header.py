#!/usr/bin/python3
""" fetches a URL an prints the X-Request-Id """


import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
    except urllib.error.URLError as e:
        print(f"Error:{e}")
