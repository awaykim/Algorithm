# 19637
import sys
n, m = map(int, sys.stdin.readline().split())
titles = dict()
def bin_search(num, arr):
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if num <= power[mid] and num > power[mid-1]: return power[mid]
        elif num > power[mid]: left = mid + 1
        else: right = mid - 1
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if int(b) in titles: continue
    titles[int(b)] = a
power = sorted(titles)
for i in range(m):
    p = int(sys.stdin.readline())
    if p <= power[0]: print(titles[power[0]])
    else: print(titles[bin_search(p, power)])
