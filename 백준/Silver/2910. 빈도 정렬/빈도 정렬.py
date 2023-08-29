n, c = map(int, input().split())
arr = list(map(int, input().split()))
d = dict()
for i in arr:
    if i in d.keys(): continue
    d[i] = arr.count(i)
d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
for key, value in d.items():
    for i in range(value):
        print(key, end=' ')