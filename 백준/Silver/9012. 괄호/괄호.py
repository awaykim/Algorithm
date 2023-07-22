N = int(input())
L = []
for i in range(N):
    L.append(list(map(str, input())))
def bracket_test(arr,n):
    flags = ['NO' for i in range(n)]
    for i in range(n):
        stack = []
        for j in range(len(arr[i])):
            if arr[i][j] == '(':
                stack.append(arr[i][j])
            else:
                if stack:
                    flag = True
                    stack.pop(0)
                else: 
                    flag = False
                    break
        if not stack and flag: flags[i] = 'YES'
        del stack
    return flags
                
for i in bracket_test(L,N):
    print(i)