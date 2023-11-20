numbers = list(map(int, input().split()))
q = 0
for num in numbers:
    q += (num ** 2) % 10
print(q % 10)