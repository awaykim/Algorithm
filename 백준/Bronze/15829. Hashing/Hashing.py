L = int(input())
string = list(input())
ans = 0
r = 31
M = 1234567891
for a in range(len(string)):
    ans += ((ord(string[a]) - ord('a') + 1) * (r ** a))
print(ans % M)