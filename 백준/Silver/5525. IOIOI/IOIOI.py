N = int(input())
M = int(input())
S = input()
target = "" 
answer = 0
length = 2 * N + 1
for i in range(length): target += "O" if i % 2 else "I"
for i in range(len(S)): answer += 1 if S[i:length+i] == target else 0
print(answer)