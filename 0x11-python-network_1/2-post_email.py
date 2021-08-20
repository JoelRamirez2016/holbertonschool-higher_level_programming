#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response"""
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    with urlopen(Request(sys.argv[1],
                 urlencode({'email': sys.argv[2]}).encode())) as response:
        print(response.read().decode())
