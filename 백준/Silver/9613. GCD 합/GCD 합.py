T = int(input())
L= [0 for _ in range(T)]
for i in range(T):
    L[i] = list(map(int, input().split()))

def solution(l):  
    def findGCD(n,m):
        if n < m : n, m = m, n
        r = n % m
        while r != 0:
            n, m = m, r
            r = n % m
        return m
    sum = 0
    for i in range(1,len(l)-1):
        for j in range(i+1, len(l)):
            sum += findGCD(l[i], l[j])
    return sum

for i in range(T):
    print(solution(L[i]))