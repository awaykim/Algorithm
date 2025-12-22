def solution(n, computers):
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
            return parent[x]
        return x
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else: 
            parent[a] = b

    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                union(i, j)
    for i in range(n):
        parent[i] = find(i)

    return len(set(parent))