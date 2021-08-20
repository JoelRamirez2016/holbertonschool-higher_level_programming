#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”"""
import sys
import requests

if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(sys.argv[1], sys.argv[2]))

    commits = r.json()

    for i in range(0, 10 if len(commits) > 10 else len(commits)):
        print("{}: {}".format(commits[i]['sha'],
              commits[i]['commit']["author"]['name']))
