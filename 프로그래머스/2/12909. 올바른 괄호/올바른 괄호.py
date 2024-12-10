def solution(s):
    answer = True
    stack = []
    for par in s:
        if par == '(':
            stack.append('*')
        else:
            if not stack: return False
            stack.pop()
    if stack: return False
        
    return True