n, m = map(int, input().split())
h = list(map(int, input().split()))

def tree_search(left, right):
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        length = 0
        for i in range(n):
            if h[i] > mid:
                length = length + (h[i] - mid)
        
        if length < m:
            right = mid - 1
        elif length == m: 
            ans = mid
            break
        else:
            ans = max(mid, ans)
            left = mid + 1
    print(ans)

tree_search(0, max(h))