'''
BFS (DFS로 해도 될 것 같아요)
**모든 도시를 방문할 수 없는 경로로 가지 않기**
- visited: 방문했을 경우 True, unavailable한 경로였을 경우 False로 -> DFS에 어울린다.
- visited: 큐에 함께 전달한다 
'''

from collections import deque

def solution(tickets):
    
    answer = []
    
    # 알파벳 순서로 정렬 
    tickets.sort(key = lambda x: (x[0], x[1]))
    
    # 현재 경로와 현재 방문한 티켓 정보 
    q = deque([(["ICN"], tickets)])
    
    while q:
        
        # 현재 경로와 티켓 정보를 가져온다
        cur_path, cur_tickets = q.popleft()
        cur = cur_path[-1]
        
        # 만약 모든 티켓을 사용했을 경우(=모든 경로 순회) return
        if not cur_tickets: 
            answer = cur_path
            break
        
        
        for ticket in cur_tickets:
            depart, arrival = ticket[0], ticket[1]
            
            # 현재 위치에서 출발하는 항공권의 경우 
            if depart == cur:
                
                # 새로운 경로와 티켓 정보를 q에 넣는다
                new_tickets = cur_tickets.copy()
                new_tickets.remove(ticket)
                
                new_path = cur_path.copy()
                new_path.append(arrival)
                
                q.append((new_path, new_tickets))
                
                
    return answer