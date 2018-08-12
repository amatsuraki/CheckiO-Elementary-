#!/usr/bin/python
# -*- Coding: utf-8 -*-
def checkio(n, m):
    x = bin(n ^ m)
#    print('x = {}'.format(x))

    return x.count('1')


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
