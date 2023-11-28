#!/usr/bin/python3
for n in range(0, 100):
    if n < 99:
        sep = ', '
    else:
        sep = '\n'
    print('{:02d}'.format(n), end=sep)
