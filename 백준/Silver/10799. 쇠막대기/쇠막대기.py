arr = list(map(str,input()))
stck = []
ans = 0
for i in range(len(arr)):
    if arr[i] == '(': 
        stck.append(arr[i])
    else: 
        stck.pop()
        if arr[i-1] == '(': 
            ans += len(stck)
        else:
            ans += 1
print(ans)