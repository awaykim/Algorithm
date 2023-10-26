from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque([(0,0)])
while q:
    x, y = q.popleft()
    val = graph[x][y]
    if val == 0: continue
    if val == -1: 
        print("HaruHaru")
        exit()
    if x + val < n: q.append((x+val, y))
    if y + val < n: q.append((x, y+val))
    graph[x][y] = 0
print("Hing")
