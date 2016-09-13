#-*- coding:utf-8 -*-
"""
if __name__ == '__main__':
    tlist = []
    head, mid, rear = 1, 0, 1
    
    for i in range(input()):
        tlist.append(head)
        mid = int(head+rear)
        head = rear
        rear = mid

    print tlist[i]
"""
tlist = []
head, mid, rear = 1, 2, 2
for i in range(1, input()):
    tlist.append(head)
    mid = int(head+rear)
    head = rear
    rear = mid

print tlist[i-1]
