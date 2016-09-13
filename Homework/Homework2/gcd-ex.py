# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def gcd(a, b):
    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r

if __name__ == '__main__':
    f = open('gcd.txt', 'r')

    for testcase in range(int(f.readline())):
        values = f.readline().split()
        print gcd(int(values[0]), int(values[1]))
        
    f.close()
