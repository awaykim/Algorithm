import sys, math
m, n = map(int, sys.stdin.readline().split())

def find_prime(a, b):
    for i in range(a, b+1):
        flag = True
        if i == 1:
            continue
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0: 
                flag = False
                break
        if flag: print(i)
    return

find_prime(m, n)