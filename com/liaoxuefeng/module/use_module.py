'a test module'

__author__ = 'sundan'
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello , %s ', args[1])
    else:
        print('Too many args')
