import sys
n, k = map(int, sys.stdin.readline().split())
def solution(n, k):
    circle = [0] * n # 0, 1, 2, 3, 4, 5, 6
    ans = []
    s = 0
    while 0 in circle:
        p = 0
        for i in range(s, n):
            if circle[i] == 1: continue
            else: p += 1
            if p == k: 
                s = i
                circle[i] = 1
                ans.append(i+1)
                break
        while p < k: 
            for i in range(n):
                if circle[i] == 1: continue
                else: p += 1
                if p == k: 
                    s = i
                    circle[i] = 1
                    ans.append(i+1)
                    break 
    print('<', end='')
    print(*ans, sep=', ', end='>')
    return


solution(n, k)