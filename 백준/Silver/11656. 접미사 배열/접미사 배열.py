s = list(map(str, input()))
li = []
while s:
    li.append("".join(s))
    s.pop(0)
li.sort()
for i in li:
    print(i)