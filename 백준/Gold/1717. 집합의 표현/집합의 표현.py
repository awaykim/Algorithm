import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

# 루트 관계를 나타내는 table
# table[i] = j == root(i) = j
table = [i for i in range(n+1)]

def find(x): # x의 루트를 찾는다.
    if x == table[x]: 
        return x
    else:
        # x의 상위 노드로부터 루트를 찾는다
        # table[x] = find(table[x])
        # return table[x]
        return find(table[x])

def union(x, y): # x와 y의 루트를 같게 만든다. (연결)
    x_root = find(x)
    y_root = find(y)
    # 두 루트 중 작은 수를 루트로 한다
    if x_root != y_root:
        table[max(x_root, y_root)] = min(x_root, y_root)



for i in range(m):
    # 포함관계 if com or 합집합
    com, a, b = map(int, input().split())
    if com == 0: # 합집합
        union(a,b)
    if com == 1: # 포함관계 확인
        if a == b or find(a) == find(b): print("YES")
        else: print("NO")