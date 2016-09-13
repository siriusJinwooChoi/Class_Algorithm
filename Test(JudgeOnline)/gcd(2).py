#-*- coding: utf-8 -*-
def gcd(a, b):
    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r

if __name__ == '__main__':
    for testcase in range(input()):
        values = raw_input().split()
        print gcd(int(values[0]), int(values[1]))
