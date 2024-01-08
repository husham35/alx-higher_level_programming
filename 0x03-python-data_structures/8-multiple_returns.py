#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first = 'None'
        length = 0
        result = (length, first)
        return result
    else:
        first = sentence[0]
        length = len(sentence)
        result = (length, first)
        return result
