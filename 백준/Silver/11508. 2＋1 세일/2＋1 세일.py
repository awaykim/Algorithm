n = int(input())
costs = [int(input()) for _ in range(n)]
costs_order = sorted(costs, reverse=True)
s = 0
for i in range(n):
    if (i + 1) % 3 == 0: continue
    s += costs_order[i]
print(s)