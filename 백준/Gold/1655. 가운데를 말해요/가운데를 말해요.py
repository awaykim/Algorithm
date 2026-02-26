import heapq
import sys

input = sys.stdin.readline

N = int(input())

# 중간값보다 작은 값들은 leftHeap에, 큰 값은 rightHeap
# 중간값 = leftHeap[0]
leftHeap = [] # 최대힙
rightHeap = [] # 최소힙

for _ in range(N):
  num = int(input())
  
  if len(leftHeap) == len(rightHeap):
    heapq.heappush(leftHeap, -num)
  else:
    heapq.heappush(rightHeap, num)

  if rightHeap and rightHeap[0] < -leftHeap[0]:
    l = heapq.heappop(leftHeap)
    r = heapq.heappop(rightHeap)
    heapq.heappush(leftHeap, -r)
    heapq.heappush(rightHeap, -l)

  print(-leftHeap[0])