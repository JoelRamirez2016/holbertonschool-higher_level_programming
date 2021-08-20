#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")

    print("Body response:\n" +
          "\t- type: {}\n".format(type(r.text)) +
          "\t- content: {}".format(r.text))
