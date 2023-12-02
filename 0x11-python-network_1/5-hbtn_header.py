#!/usr/bin/python3
""" same as task 1 but using requests """

import sys
import requests

if __name__ == '__main__':

    try:
        response = requests.get(sys.argv[1])
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
    except requests.RequestException as e:
        print(f"Error: {e}")
