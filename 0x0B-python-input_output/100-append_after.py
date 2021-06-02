#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r") as f:
        contents = f.readlines()

    contents = list(
                   map(
                       lambda l: l + new_string if search_string in l else l,
                       contents
                   )
               )

    with open(filename, "w") as f:
        contents = "".join(contents)
        f.write(contents)
