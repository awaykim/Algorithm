import sys
n = int(sys.stdin.readline())

def solution(n):
    stack = []
    ops = []
    p = 1
    for i in range(n):
        e = int(sys.stdin.readline())
        if stack: 
            top = stack[-1]
            if top == e:
                stack.pop()
                ops.append('-')
            elif top < e:
                for j in range(p, e):
                    stack.append(j)
                    ops.append('+')
                ops.append('+')
                ops.append('-')
                p = e + 1
            else: 
                print('NO')
                return
        else:
            for j in range(p, e):
                stack.append(j)
                ops.append('+')
            ops.append('+')
            ops.append('-')
            p = e + 1
    for _ in ops:
        print(_)
            
    


solution(n)