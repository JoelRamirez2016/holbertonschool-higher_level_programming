#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)"""
import urllib.request
import sys
import urllib.error
from urllib.request import Request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(Request(sys.argv[1])) as response:
            print(response.read().decode())
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
