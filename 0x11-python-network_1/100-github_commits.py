#!/usr/bin/python3
"""  fetches commits from a githun repo  """
import requests
import sys

if __name__ == "__main__":
    i = 0
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    for commit in sorted(response.json(), key=lambda c: c.get('commit')
                         .get('author').get('date'), reverse=True):
        print(commit.get('sha') + ": ", end="")
        print(commit.get('commit').get('author').get('name'))
        i += 1
        if i == 10:
            break
