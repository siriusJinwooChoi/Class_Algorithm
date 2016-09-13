# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def dynamic():
    data = []
    n = int(raw_input())
    for k in range(n):
        a = len(data)
        s = sys.getsizeof(data)
        print('length: {0:3d}, bytes: {1:4d}'.format(a,s))
        data.append(None)

if __name__ == '__main__':
    dynamic()
