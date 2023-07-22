N, S = map(int, input().split())
L = list(map(int, input().split()))

def partial_sum(arr, sum):
    a = b = 0
    sums = []
    tmp = arr[a]
    while True:
        while tmp >= sum:
            sums.append(b-a+1)
            tmp -= arr[a]
            a += 1
        b += 1
        if b == len(arr): break
        tmp += arr[b]
    if sums: 
        return min(sums)
    else: return 0

print(partial_sum(L, S))