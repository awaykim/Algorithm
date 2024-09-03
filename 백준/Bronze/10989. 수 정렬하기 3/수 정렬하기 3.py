import sys
n = int(sys.stdin.readline())
li = [0] * 10001
for i in range(n):
    num = int(input())
    li[num] += 1
for i in range(1, 10001):
    for _ in range(li[i]):
            print(i)