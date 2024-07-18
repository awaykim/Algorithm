def nCr(arr, r):
    if r == 0:
        return[[]]
    res = []
    for i in range(len(arr)):
        element = arr[i]
        rest = arr[i + 1:]
        for c in nCr(rest, r-1):
            res.append([element]+c)
    return res
n, m = map(int, input().split())
cards = list(map(int, input().split()))
group = nCr(cards, 3)
opt = 0
for g in group:
    if sum(g) <= m and m - opt > m - sum(g):
        opt = sum(g)
print(opt)
