#!/usr/bin/python3
def print_tebahpla():
    for i in range(122, 96, -1):
        i = i - 32 if i % 2 else i
        print('{}'.format(chr(i)), end='')


print_tebahpla()
