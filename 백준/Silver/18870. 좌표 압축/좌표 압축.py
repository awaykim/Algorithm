import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
sort_num = sorted(set(numbers))
dic_num = dict()
for i in range(len(sort_num)):
    dic_num[sort_num[i]] = i
for i in numbers:
    print(dic_num[i], end=' ')