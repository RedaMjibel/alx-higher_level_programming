#!/usr/bin/python3
""" send POST request to a URL an prints the response """

import requests
import sys

if __name__ == '__main__':
    data = {"email": sys.argv[2]}
    try:
        response = requests.post(sys.argv[1], data=data)
        print(response.text)
    except requests.RequestException as e:
        print(f"Error: {e}")
