n, m = map(int, input().split())
# knows[0] = 아는 사람의 수. knows[1:] = 아는 사람의 번호
knows = list(map(int, input().split()))[1:]
# parties[i][0] = 파티 참여 인원. parties[i][1:] = 파티 참여자
parties = [list(map(int, input().split())) for _ in range(m)]
# 구라파티의 수
cnt = 0
# 그룹
group = [(i) for i in range(n+1)]

def find(x): # x번 노드의 루트를 찾는다
    if group[x] == x: 
        return x
    else: # 현재 나의 루트인 노드의 루트를 찾는다
        return find(group[x])   
            
def union(a,b): # a와 b를 합친다
    a_root = find(a)
    b_root = find(b)
    # b의 루트 노드를 a의 루트 노드로 지정한다. 
    # 아는 사람을 루트로 지정한다
    if a_root in knows:
        group[b_root] = a_root
    elif b_root in knows:
        group[a_root] = b_root
    # 둘 다 모르는 사람이라면 작은 쪽을 루트로 지정한다.
    else:
        group[max(a_root,b_root)] = min(a_root, b_root)

for i in range(m):
    for j in range(1, parties[i][0]):
        union(parties[i][j], parties[i][j+1])

for i in range(m):
    for j in parties[i][1:]:
        if find(j) in knows: break
    else:
        cnt +=1 
print(cnt)
