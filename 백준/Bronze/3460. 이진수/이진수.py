T = int(input())
for i in range(T):
    ones = []
    n = int(input())
    i = 0
    while n > 0:
        if n % 2 == 1:
            ones.append(i)
        i += 1
        n //= 2
    print(*ones)