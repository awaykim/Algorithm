# 17413
import sys
string = sys.stdin.readline().rstrip() + ' '
li = []
flag = False
for s in string:
    if s == '<': 
        flag = True
        if li:
            st = "".join(li)
            print(st[::-1], end='')
            li.clear()
    if flag: 
        print(s, end='')
        if s == '>': flag = False
    else:
        if s == ' ':
            st = "".join(li)
            print(st[::-1], end=' ')
            li.clear()
        else: 
            li.append(s)