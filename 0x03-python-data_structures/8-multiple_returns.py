#!/usr/bin/python3
def multiple_returns(sentence):
    result = (len(sentence), sentence[0]) if sentence else (0, None)
    return result
