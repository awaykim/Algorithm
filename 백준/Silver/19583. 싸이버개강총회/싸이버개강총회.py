import sys
input = sys.stdin.readline

S, E, Q = map(str, input().split())
start = int(''.join(S.split(":")))
end = int(''.join(E.split(":")))
quit = int(''.join(Q.split(":")))

hashmap = dict()
ans = 0
while True:
  line = input().strip()
  if not line:
        break
  t, n = map(str, line.split())
  time = int(''.join(t.split(":")))
  if time <= start: hashmap[n] = 1
  elif end <= time <= quit and n in hashmap.keys() and hashmap[n] == 1:
    hashmap[n] = 0
    ans += 1

print(ans)