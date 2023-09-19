k = int(input())
c = int(input())
for _ in range(c):
    m, n = map(int, input().split())
    if abs(m-n) < 2: 
        print(1)
        continue
    if m > n:
        chance = k - m
        if chance + n >= m - 2:
            print(1)
        else: print(0)
    else:
        chance = k - n
        if chance + m >= n - 1:
            print(1)
        else: print(0)
    
    