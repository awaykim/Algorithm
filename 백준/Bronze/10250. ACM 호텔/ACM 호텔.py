t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    num = n // h + 1
    if floor == 0: 
        floor = h
        num -= 1
    if num < 10: 
        print(str(floor)+'0'+str(num))
    else:
        print(str(floor)+str(num))
