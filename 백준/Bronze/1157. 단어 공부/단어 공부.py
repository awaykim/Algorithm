word = input().upper()


def solution(w):
    alp = list(set(w))
    cnt = []
    for s in alp:
        cnt.append(w.count(s))
    
    if cnt.count(max(cnt)) > 1:
        return '?'
    else: 
        return alp[cnt.index(max(cnt))]

print(solution(word))