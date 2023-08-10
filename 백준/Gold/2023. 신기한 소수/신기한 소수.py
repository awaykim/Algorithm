import sys, math
n = int(sys.stdin.readline())

def solution(n):
    def is_prime(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0: return False
        return True
    primes = (2, 3, 5, 7)
    for _ in range(n-1):
        tmp = []
        for p in primes:
            for i in range(1, 10, 2):
                w = p * 10 + i
                if is_prime(w): tmp.append(w)
        primes = tuple(tmp)
    for i in primes:
        print(i)
    return

solution(n)