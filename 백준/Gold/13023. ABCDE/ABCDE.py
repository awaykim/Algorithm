
import sys
sys.setrecursionlimit(10**8)
n, m = map(int, sys.stdin.readline().split())
rel = [[i] for i in range(n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    rel[a].append(b)
    rel[b].append(a)

def friend_dfs(v, friend):
    friend.append(v)
    for i in range(1, len(rel[v])):
        if rel[v][i] not in friend:
            if len(friend) == 4:
                print(1)
                exit()
            # print(v, rel[v][i], friend)
            friend_dfs(rel[v][i], friend)
            friend.pop()               
    return friend

for i in range(n):
    friend_dfs(i, [])
print(0)



