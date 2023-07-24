import sys
N = int(input())

def solution(n):
    table = [0] * (n + 1)
    for i in range(1, len(table)):
        table[i] = i - 1
    for i in range(2, len(table)):
        sub_res = [sys.maxsize] * 3
        if i % 3 == 0: sub_res[0] = table[i//3] + 1
        if i % 2 == 0 : sub_res[1] = table[i//2] + 1
        sub_res[2] = table[i-1] + 1
        for j in range(3):
            table[i] = min(table[i], sub_res[j])
    return table[n]

print(solution(N))