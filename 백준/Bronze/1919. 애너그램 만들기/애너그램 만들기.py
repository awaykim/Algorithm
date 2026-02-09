s1 = list(input())
s2 = list(input())

i = 0
while i < len(s1):
  t =  s1[i]
  if s1[i] in s2:
    s1.remove(t)
    s2.remove(t)
    i -=1
  i += 1

print(len(s1)+len(s2))