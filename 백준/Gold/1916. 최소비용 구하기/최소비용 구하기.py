import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

buses = list([INF] * (n+1) for _ in range(n+1))
for i in range(m):
    x, y, z = map(int, input().split())
    if buses[x][y] > z:
        buses[x][y] = z
start, end = map(int, input().split())

distance = [INF] * (n+1) # 최단 거리 테이블

hq = []
distance[start] = 0 # 최단 거리 테이블 초기화
heapq.heappush(hq, (distance[start], start)) # hq에 가중치와 현재 위치

while hq:
    weight, node = heapq.heappop(hq)
    for i in range(1, n+1):
        # 이미 처리 된 노드일 경우 Pass 
        if distance[node] < weight: continue
        # 새로운 루트가 더 짧을 경우 업데이트
        if weight + buses[node][i] < distance[i]:
            distance[i] = weight + buses[node][i]
            heapq.heappush(hq, (distance[i], i))

print(distance[end])