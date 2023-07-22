a, r= [0 for i in range(10)], [0 for i in range(10)]
for i in range(10):
    a[i] = int(input())
    r[i] = a[i] % 42
s = set(r)
print(len(s))