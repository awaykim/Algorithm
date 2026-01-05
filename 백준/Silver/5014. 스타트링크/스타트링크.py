from collections import deque 


floor, start, goal, up, down = map(int, input().split())

visited = [0] * (floor + 1)
answer = 0

q = deque([(start, 0)])

while q:
  c, w = q.popleft()
  if c == goal: 
    answer = min(answer, w) if answer else w
    continue
  nw = w + 1
  uc = c + up
  dc = c - down
  if uc != start and uc <= floor and (visited[uc] > nw or not visited[uc]):
      visited[uc] = nw
      q.append((uc, nw))
  if dc != start and 0 < dc and (visited[dc] > nw or not visited[dc]):
      visited[dc] = nw
      q.append((dc, nw))


if start == goal: 
  print(0)
else:
  print(answer) if answer else print("use the stairs")

  