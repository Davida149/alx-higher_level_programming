#!/usr/bin/python3
for char in range(26):
    if char != 16 and char != 4:
        print("{:s}".format(chr(char + ord("a"))), end='')
