#!/usr/bin/python3
""" fetches 10 commits from a repository """

import requests
import sys

if __name__ == "__main__":
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                            .format(argv[1], argv[2]))
    i = 0
    for commit in sorted(response.json(), key=lambda c: c.get('commit')
                         .get('author').get('date'), reverse=True):
        print(commit.get('sha') + ": ", end="")
        print(commit.get('commit').get('author').get('name'))
        i = i + 1
        if i == 10:
        break
