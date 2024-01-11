n, m = map(int, input().split())
array = list(map(int, input().split()))
start, end = 0, 0
count = 0
while end < n:
    prefix_sum = sum(array[start:end+1])
    if prefix_sum < m:
        end += 1
    elif prefix_sum > m:
        start += 1
    else: 
        count += 1
        end += 1
print(count)
