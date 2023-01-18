#!/usr/bin/python3
"""script that takes your Github credentials (username and password) and uses
the Github API to display your id"""

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pssword = sys.argv[2]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=(user, pssword))
    req_json_rep = r.json()

    print(req_json_rep.get("id", "None"))
