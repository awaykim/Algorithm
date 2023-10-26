n = int(input())
sizes = [list(map(int, input().split())) for _ in range(n)]
rank = [1] * n
for i in range(n):
    for j in range(n):
        if i == j: continue
        if sizes[j][0] > sizes[i][0] and sizes[j][1] > sizes[i][1]:
            rank[i] += 1
print(*rank)
