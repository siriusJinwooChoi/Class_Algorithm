# -*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

def ex2():
    tlist = raw_input().split()

    #First Solution - Using Bubble sort
    for a in range(len(tlist)-1):
        for b in range(1, len(tlist)-a):
            if int(tlist[b-1]) > int(tlist[b]):
                tlist[b-1], tlist[b] = tlist[b], tlist[b-1]
    print tlist[0]
    print tlist[len(tlist)-1]
    
    #Second Solution - just Solution(To find for min, max values)
    """
    mini, maxi = int(tlist[0]), int(tlist[0])
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
    sentence = '       hello apple '
    sentence = sentence.replace(" ", "")
    print sentence
    ex2()
