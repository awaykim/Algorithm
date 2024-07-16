import math
n = int(input())
num = list(map(int, input().split()))
sum = 0
for i in num:
    if i < 2: continue
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0: 
            is_prime = False
            break
    if is_prime: sum+= 1            
print(sum)