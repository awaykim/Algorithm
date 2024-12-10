import math 

def solution(progresses, speeds):
    answer = []
    days = [] 
    cnt = 1
    for p,s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        if not days:
            days.append(day)
            continue
        if days[-1] >= day:
            cnt += 1
        else:
            answer.append(cnt)
            days.pop()
            days.append(day)
            cnt = 1
    if cnt:
        answer.append(cnt)
        
    return answer