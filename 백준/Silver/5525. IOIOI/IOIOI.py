import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
P = "IOI"
i = 0
j = 3
ans = 0
Pcontinue = 0

while True:
  if j >= len(S): break

  if S[i:j] == P: 
    Pcontinue += 1
    if Pcontinue < N: 
      i += 2
      j += 2
      continue
    else:
      ans += 1
      Pcontinue -= 1
      i += 2
      j += 2
  else:
    i += 1
    j += 1
    Pcontinue = 0

print(ans)