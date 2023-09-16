n = int(input())
table = list(list(map(int, input().split())) for _ in range(n))
for i in range(1, n):
    table[i][0] += min(table[i-1][1], table[i-1][2]) 
    table[i][1] += min(table[i-1][0], table[i-1][2]) 
    table[i][2] += min(table[i-1][0], table[i-1][1]) 
print(min(table[n-1][0], table[n-1][1], table[n-1][2]))