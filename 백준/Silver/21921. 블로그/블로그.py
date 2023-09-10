n, x = map(int, input().split())
v = list(map(int, input().split()))
sum = 0
for i in range(0, x):
    sum += v[i]
max_v, max_count = sum, 1
s, e = 0, x
while True:
    if e > n - 1: break
    sum = sum - v[s] + v[e]
    if max_v > sum: pass
    elif max_v == sum: max_count += 1
    else: 
        max_v = sum
        max_count = 1
    s += 1
    e += 1
    
if max_v == 0: print('SAD')
else: 
    print(max_v)
    print(max_count)
