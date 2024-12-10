from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([(i,p) for i,p in enumerate(priorities) ])
    while True:
        loc, pri = q.popleft()
        if any(pri < p[1] for p in q):
            q.append((loc,pri))
        else:
            answer += 1
            if loc == location: return answer