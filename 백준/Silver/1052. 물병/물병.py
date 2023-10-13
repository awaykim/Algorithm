n, k = map(int, input().split())
num = n
while bin(n).count('1') > k:
    exp = bin(n)[::-1].index('1')
    n += 2**exp
print(n - num)