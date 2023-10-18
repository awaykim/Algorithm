from itertools import permutations
n = int(input())
numbers = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3))
for _ in range(n):
    removes = 0
    q, strikes, balls = map(int, input().split())
    q = list(str(q)) 
    for i in range(len(numbers)):
        s_cnt, b_cnt = 0, 0
        i -= removes
        for j in range(3):
            if q[j] == numbers[i][j]: s_cnt += 1
            elif q[j] in numbers[i]: b_cnt +=1
        if s_cnt != strikes or b_cnt != balls:
            numbers.remove(numbers[i])
            removes += 1
print(len(numbers))