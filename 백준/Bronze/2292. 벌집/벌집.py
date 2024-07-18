n = int(input())
sum = 1
cnt = 1
while n > sum:
    sum += cnt * 6
    cnt += 1
print(cnt)