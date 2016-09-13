# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def ex2():
    s = raw_input()
    tlist = s.split()

    #First Solution - Using Bubble sort
    for a in range(len(tlist)-1):
        for b in range(1, len(tlist)-a):
            if int(tlist[b-1]) > int(tlist[b]):
                temp = tlist[b-1]
                tlist[b-1] = tlist[b]
                tlist[b] = temp
    print tlist[0]
    print tlist[len(tlist)-1]
    
    #Second Solution - just Solution(for min, max values)
    """
    mini = int(tlist[0])
    maxi = int(tlist[0])
    for i in range(1, len(tlist)):
        if int(tlist[i]) < mini:
            mini = int(tlist[i])
        else:
            if maxi < int(tlist[i]):
                maxi = int(tlist[i])
    print mini
    print maxi
    """

if __name__ == '__main__':
    ex2()
