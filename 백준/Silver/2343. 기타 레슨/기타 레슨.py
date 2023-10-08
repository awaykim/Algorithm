n, m = map(int, input().split())
arr = list(map(int, input().split()))
left, right = max(arr), sum(arr)
ans = 0
while left <= right:
    mid = (left+right) // 2
    count, size = 0, 0
    for i in range(n):
        if size + arr[i] > mid:
            count += 1
            size = 0
        size += arr[i]
    if size: count += 1
    if count > m: left = mid + 1
    else: 
        right = mid - 1
        ans = mid
print(ans)