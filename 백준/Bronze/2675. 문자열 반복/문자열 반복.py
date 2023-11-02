t = int(input())
for _ in range(t):
    r, s = map(str, input().split())
    r = int(r)
    for w in s:
        print(w*r, end='')
    print()