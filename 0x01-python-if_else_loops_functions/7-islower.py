#!/usr/bin/python3
def islower(c):
    for lower in range(ord('a'), ord('z') + 1):
        if ord(c) == lower:
            return True
        else:
            False
