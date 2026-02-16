N = int(input())
switches = list(map(int, input().split()))
M = int(input())
students = []
for _ in range(M):
  students.append(tuple(map(int, input().split())))

for s in students:
  sex, num = s

  if sex == 1:
    i = 1
    while num*i-1 < N:
      switches[num*i-1] = 1 - switches[num*i-1]
      i += 1

  else:
    j = 0
    while num+j-1 < N and 0 <= num-j-1 and switches[num-j-1] == switches[num+j-1]:
      j += 1
    j -= 1
    for k in range(num-j-1, num+j):
      switches[k] = 1 - switches[k]

for i in range(N):
    if i and i % 20 == 0:
        print()
    print(switches[i], end=" ")