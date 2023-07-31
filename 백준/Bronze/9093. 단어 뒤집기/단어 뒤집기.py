import sys
T = int(sys.stdin.readline())

def solution():
   for i in range(T):
    string = list(sys.stdin.readline().split())
    stack = []
    for word in string:
        for ch in word: stack.append(ch)
        while stack: print(stack.pop(), end='')
        print(end=' ')
    print()

solution()