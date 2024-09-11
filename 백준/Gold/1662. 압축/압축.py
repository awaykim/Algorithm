import sys
input = sys.stdin.readline
s = input().rstrip()
stack1 = [] # K 저장
stack2 = [] # 현재 단계의 총 글자수 

leng = 0

for i in range(len(s)):
    if s[i] == '(':
        leng -= 1
        stack1.append(int(s[i-1]))
        stack2.append(leng)
        leng = 0
    elif s[i] == ')':
        leng = leng * stack1.pop() + stack2.pop() 
    else:
        leng += 1
    
print(leng)
