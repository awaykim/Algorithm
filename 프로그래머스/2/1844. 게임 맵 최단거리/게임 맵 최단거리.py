def solution(maps):
    from collections import deque
    answer = 0
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque([(0,0)])
    visited[0][0] = 1
    if not maps[n-1][m-2] and not maps[n-2][m-1]: 
        return -1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            if answer:
                answer = min(answer, visited[x][y])
            else: 
                answer = visited[x][y]
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and not visited[nx][ny]: 
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    if not visited[n-1][m-1]:
        return -1
    return answer