# 2840
n, k = map(int, input().split())
li = ['?'] * n
t = 0
for i in range(k):
    number, s = map(str, input().split())
    number = int(number)
    t = (t - number) % n
    if li[t] == '?': 
        if s in li:
            print('!')
            exit()
        else: li[t] = s
    else: 
        if li[t] != s: 
            print('!')
            exit()
    if i is k-1: 
        answer = li[t:] + li[:t]
print(''.join(answer))