from collections import deque
def solution(user_id, banned_id):
    
    answer = 0
    
    mapped_id = [[] for _ in range(len(banned_id))]
    for i, ban in enumerate(banned_id):
        for j, user in enumerate(user_id):
            flag = True
            if len(ban) != len(user):
                continue
            for k, ch_ban in enumerate(ban):
                if ch_ban.isalnum() and ch_ban != user[k]:
                    flag = False
                    break
            if flag: 
                mapped_id[i].append(j)

    q = deque()
    for i in mapped_id[0]:
        arr = [i]
        q.append(arr)
    
    sets = []
    
    while q:
        ids = q.popleft()
        col = len(ids)
        if col == len(mapped_id): 
            if set(ids) not in sets:
                sets.append(set(ids))
                answer += 1
            continue
        for id in mapped_id[col]:
            if id not in ids:
                new_ids = ids + [id]  
                q.append(new_ids)

    return answer