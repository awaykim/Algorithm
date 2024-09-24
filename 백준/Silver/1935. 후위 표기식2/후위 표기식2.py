n = int(input())
exp = list(input())
lst = []
stack = []
ans = 0
for i in range(n):
    lst.append(int(input()))

for e in exp:
    if e.isalpha():
        stack.append(lst[ord(e)-ord('A')])
        continue
    back = stack.pop()
    front = stack.pop()
    if e == '*':
        stack.append(front*back)
    elif e == '+':
        stack.append(front+back)
    elif e == '-':
        stack.append(front-back)
    elif e == '/':
        stack.append(front/back)

print("{:.2f}".format(stack[0]))