#!/usr/bin/python3
"""This module define the function text_indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text (str): text to print

    Raises:
        TypeError: if text not is str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = ""

    for j in range(0, len(text)):
        if text[j] in ".?:":
            s += text[j] + "\n\n"
        elif not (text[j] == " " and (s == "" or s[-1] == "\n" or
                  all(spaces_bt(text[j:])))):
            s += text[j]
    print(s, end="")


def spaces_bt(t):
    """Return a next "\n" coincident in string of spaces
    Args:
        t (str): string with spaces
    """
    cond = []
    for c in t:
        if c == " ":
            cond.append(True)
        elif c == "\n":
            cond.append(True)
            break
        else:
            cond.append(False)
            break
    return cond
