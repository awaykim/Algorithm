import itertools
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
nCm = list(itertools.combinations(arr, m))
for i in range(len(nCm)):
    print(*nCm[i])