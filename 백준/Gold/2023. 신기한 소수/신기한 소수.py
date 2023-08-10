import sys, math
n = int(sys.stdin.readline())
def solution_2(n):
    def is_prime(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0: return False
        return True
    def dfs(num):
        if len(str(num)) == n: print(num)
        for i in range(1, 10, 2):
            candidate = num * 10 + i
            if is_prime(candidate): dfs(candidate)
        return
    dfs(2)
    dfs(3)
    dfs(5)
    dfs(7)
    return

solution_2(n)