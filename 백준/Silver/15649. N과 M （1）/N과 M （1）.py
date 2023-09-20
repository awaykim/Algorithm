import itertools
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
nPm = list(itertools.permutations(arr, m))
for i in range(len(nPm)):
    print(*nPm[i], end="")
    print()