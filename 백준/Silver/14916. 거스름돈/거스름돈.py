import sys

coins = [2,5]
n = int(input())


def solution(coins, change):
    table = [sys.maxsize] * (n + 1)
    table[0] = 0

    for i in range(1, change + 1):
        for j in range(len(coins)):
            if coins[j] > i: continue
            else:
                table[i] = min(table[i], table[i - coins[j]] + 1)

    if table[change] == sys.maxsize: return -1
    else: return table[change]

      

print(solution(coins, n))