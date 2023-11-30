#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    len = len(argv)
    if len == 1:
        print("0 arguments.")
    elif len == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len - 1))
    for i in range(1, len):
        print("{}: {}".format(i, argv[i]))
