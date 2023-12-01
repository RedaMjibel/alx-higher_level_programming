#!/usr/bin/python3
""" send POST request to a URL an prints the response """

import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == '__main__':
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    try:
        with urllib.request.urlopen(sys.argv[1], data=data) as response:
            body = response.read().decode('utf-8')
            if body:
                print(body)
    except urllib.error.URLError as e:
        print(f"Error: {e}")
