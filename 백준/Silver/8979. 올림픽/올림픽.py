n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]
tmp_li = []
for i in range(n):
    tmp_li.append(medals[i][0])
index = tmp_li.index(k)
rank = 1

for i in range(n):
    if i == index  : continue
    
    if medals[i][1] > medals [index][1]:
        rank = rank + 1
    elif medals[i][1] == medals [index][1]:
        if medals[i][2] > medals [index][2]:
            rank = rank + 1
        elif medals[i][2] == medals [index][2]:
            if medals[i][3] > medals [index][3]:
                rank = rank + 1
            
print(rank)