import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())


def powr(x, r, c): 
    if r == 1:
        return x % c
    else:
        new = powr(x, r//2,c)
        if r % 2 == 0:
            return (new*new) % c
        else:
            return (new*new*x) % c 

print(powr(a,b,c))