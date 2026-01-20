N = int(input())
pos, neg = [], []
ones = 0
zeros = 0

for _ in range(N):
    x = int(input())
    if x > 1:
        pos.append(x)
    elif x == 1:
        ones += 1
    elif x == 0:
        zeros += 1
    else:
        neg.append(x)

pos.sort(reverse=True)
neg.sort()

ans = ones  # 1은 무조건 더함

# 양수(2 이상) 큰 것끼리 곱
for i in range(0, len(pos) - 1, 2): ans += pos[i] * pos[i + 1]

# 음수 작은 것끼리 곱
for i in range(0, len(neg) - 1, 2): ans += neg[i] * neg[i + 1]

# 양수 나머지
if len(pos) % 2: ans += pos[-1]

# 음수 나머지
if len(neg) % 2:         
    if zeros == 0:        # 0 없으면 그냥 더해야 함
        ans += neg[-1]    # 0 있으면 neg[-1]*0으로 “버림” (추가 안 함)

print(ans)
