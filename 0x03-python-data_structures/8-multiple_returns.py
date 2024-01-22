#!/usr/bin/python3
def multiple_returns(sentence):
    numsofchar = len(sentence)
    if numsofchar == 0:
        first_char = "None"
    else:
        first_char = sentence[0]
    return numsofchar, first_char
