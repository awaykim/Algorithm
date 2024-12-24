import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        if scoville[0] >= K: break
        if len(scoville) == 1: return -1
        new = heapq.heappop(scoville) +2*heapq.heappop(scoville)
        answer += 1
        heapq.heappush(scoville, new)
    return answer