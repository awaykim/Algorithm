n, m = map(int, input().split())

def gcd_and_lcm(a, b):
    ab = a*b
    if a < b: a, b = b, a
    while b != 0:
       r = a % b
       a = b
       b = r
    gcd = a
    lcm = ab // gcd
    print(gcd)
    print(lcm)
    return

gcd_and_lcm(n,m)