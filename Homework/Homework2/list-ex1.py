# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def ex1():
    s = raw_input()
    print s
    s = s.split()
    print s
    s.sort()
    print s

if __name__ == '__main__':
    ex1()
