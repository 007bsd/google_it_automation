#!/usr/bin/env python3

def character_frequency(filename):
    """"print the character frequency in a file"""
    try:
        f = open(filename)
    except OSError:
        return None

    characcters  = {}
    for line in f:
        for char in line:
            characcters[char] = characcters.get(char, 0) +1
    f.close()
    return characcters
character_frequency("z")