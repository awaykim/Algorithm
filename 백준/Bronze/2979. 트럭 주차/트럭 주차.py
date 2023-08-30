a, b, c = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(3)]
info = [0] * 100
for i in range(3):
    for j in range(li[i][0] - 1, li[i][1] - 1):
        info[j] += 1
one_fee = a * info.count(1)
two_fee = b * info.count(2) * 2
three_fee = c * info.count(3) * 3
print(one_fee + two_fee + three_fee)