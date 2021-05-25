#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = ""

    for j in range(0, len(text)):
        if text[j] in ".?:":
            s += text[j] + "\n\n"
        elif not (text[j] == " " and (s == "" or s[-1] == "\n")):
            s += text[j]
    print(s, end="")
