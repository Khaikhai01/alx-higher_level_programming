#!/usr/bin/python3
import sys
a = len(sys.argv)
#print(a, 'arguments:')
#print('Arguments passed:', end=' ')
for n in range(0, a):
    if n == 0 and n < 1:
        print(f'{n} arguments.')
    else:
        print(f'{n} arguments:')
for i in range(1, a):
    print(f'{i}:', sys.argv[i])


