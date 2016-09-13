# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def ex3():
    testlist = []
    
    n = int(raw_input())
    for i in range(0, n+1):
        testlist.append(fibo(i))

    print testlist[n]

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

if __name__ == '__main__':
    ex3()
