#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for c in str:
        upper_str += chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c
    print("{}".format(upper_str))
