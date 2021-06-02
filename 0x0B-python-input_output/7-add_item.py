#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""7-add_item
This script reads a JSON file and saves to it the arguments from the terminal.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
if __name__ == '__main__':
    args = sys.argv[1:]
    filename = "add_item.json"
    try:
        ls = load_from_json_file(filename)
    except Exception:
        ls = []
    ls.extend(args)
    save_to_json_file(ls, filename)
