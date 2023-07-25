import sys
N = int(input())
L = ['_' for _ in range(N)]
for i in range(N):
    L[i] = sys.stdin.readline().strip()


def solution(arr, n):
    cnt = 0
    for i in range(n):
        stck = []
        for element in arr[i]:
            if stck and stck[-1] == element:
                stck.pop()
            else: stck.append(element)
        if not stck: cnt += 1
        del stck
    return cnt

print(solution(L, N))