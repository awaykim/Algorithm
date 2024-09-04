T = int(input())
for _ in range(T):
    p = list(input())
    n = int(input())
    num_str = input()
    arr = num_str.strip('[]')
    if arr: arr = list(map(int, arr.split(',')))

    flag = 0
    for command in p:
        if command == 'R': 
            flag = -1 if not flag else 0
        else: 
            if not arr: 
                print('error')
                flag = 1
                break
            arr.pop(flag)
    if flag == 1: continue
    if flag: arr = arr[::-1]
    print(f"[{','.join(map(str, arr))}]")