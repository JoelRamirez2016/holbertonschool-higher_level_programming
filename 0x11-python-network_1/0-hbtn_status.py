#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:\n" +
              "\t- type: {}\n".format(type(body)) +
              "\t- content: {}\n".format(body) +
              "\t- utf8 content: {}".format(body.decode('utf-8')))
