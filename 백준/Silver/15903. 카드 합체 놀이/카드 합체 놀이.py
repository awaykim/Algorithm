import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapq.heapify(arr)
for _ in range(m):
  card1 = heapq.heappop(arr)
  card2 = heapq.heappop(arr)
  heapq.heappush(arr, card1+card2)
  heapq.heappush(arr, card1+card2)

print(sum(arr))