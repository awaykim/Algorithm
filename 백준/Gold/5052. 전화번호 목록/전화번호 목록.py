import sys
T = int(input())
L = ['_'] * T
for i in range(T):
    L[i] = ['_' for _ in range(int(input()))]
    for j in range(len(L[i])):
        L[i][j] = sys.stdin.readline().strip()

def solution(arr):
    arr.sort(key=lambda x: len(x))
    flag = True
    n = len(arr)
    for i in range(n-1):
        if not flag: break
        tel = arr[i]
        length = len(tel)
        for j in range(i+1, n):
            other = arr[j]
            if length == len(other): continue
            if tel == other[:length]:
                flag = False
                break
    if flag: return 'YES'
    else: return 'NO'

for i in range(T):
    print(solution(L[i]))