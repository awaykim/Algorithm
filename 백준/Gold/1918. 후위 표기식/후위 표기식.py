infix = list(input())

def in_to_post(arr):
    stack = []
    postfix = []
    for i in range(len(arr)):
        op = arr[i]
        if op.isalpha():
            postfix.append(op)
        else:
            if op == '(':
                stack.append(op)
            elif op == ')':
                while True:
                    if stack[-1] == '(':
                        stack.pop(-1)
                        break
                    postfix.append(stack.pop(-1))
                    
            elif op == '-' or op == '+':
                while stack:
                    if stack[-1] =='(': break
                    else:
                        postfix.append(stack.pop(-1))
                stack.append(op)
            else:
                while stack:
                    if stack[-1] == '*' or stack[-1] == '/':
                        postfix.append(stack.pop(-1))
                    else: break
                stack.append(op)
    while stack:
        postfix.append(stack.pop(-1))
    return ''.join(s for s in postfix)


print(in_to_post(infix))