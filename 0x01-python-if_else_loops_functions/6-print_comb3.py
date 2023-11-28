#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        sep = ', '
        if i == 8:
            sep = '\n'
        print('{:d}{:d}'.format(i, j), end=sep)
