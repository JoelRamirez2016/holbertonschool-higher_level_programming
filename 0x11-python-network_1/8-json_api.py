#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import sys
import requests

if __name__ == "__main__":
    r = requests.post("http://0.0.0.0:5000/search_user",
                      data={'q': "" if len(sys.argv) == 1 else sys.argv[1]})
    try:
        j = r.json()
        print("[{}] {}".format(j['id'], j['name']) if j != {} else "No result")
    except Exception:
        print("Not a valid JSON")
