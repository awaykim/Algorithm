from collections import deque
def solution(numbers, target):
    # init 
    answer = 0
    q = deque([])
    q.append((numbers[0],0))
    q.append((numbers[0]*(-1), 0))
    
    # BFS
    while q:
        cur, idx = q.popleft()
        if idx == len(numbers)-1:
            if cur == target: answer += 1
            continue
        q.append((cur+numbers[idx+1], idx+1))
        q.append((cur-numbers[idx+1], idx+1))
        
    return answer