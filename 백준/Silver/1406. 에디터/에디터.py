# 1406
import sys
string = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

def solution(s, n):
    front = list(string)
    back = []
    for i in range(n):
        # print(front, back)
        command = sys.stdin.readline().rstrip()
        if command[0] == 'P': 
            front.append(command[2:])
        elif command[0] == 'L': 
            if front:
                back.append(front.pop(-1))
        elif command[0] == 'D': 
            if back:
                front.append(back.pop())
        else:
            if front:
                front.pop(-1)
    back.reverse()
    ans = "".join(front) + "".join(back)
    print(ans)
    return

solution(string, n)