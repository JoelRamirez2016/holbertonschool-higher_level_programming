#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    r = requests.get("https://api.github.com/user",
                     auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json().get("id"))
