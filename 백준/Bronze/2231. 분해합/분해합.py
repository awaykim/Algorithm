def findCon(n):
    ans = 0
    num = int(n)
    for i in range(num):
        con = i 
        for j in str(i):
            con = con + int(j)
        if con == num: 
            ans = i
            break   
    print(ans) 
n = input()
findCon(n)
