import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = list(input().rstrip())
new = []

for i in range(len(string)):
    cur = string[i]
    new.append(cur)
    if cur == bomb[-1] and len(bomb) <= len(new) and new[-len(bomb):] == bomb:
        del new[-len(bomb):]

if new: ans = ''.join(new)
else: ans ="FRULA"

print(ans)


