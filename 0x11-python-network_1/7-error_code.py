#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
the body of the response"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.text if r.status_code >= 400 else r.status_code)
