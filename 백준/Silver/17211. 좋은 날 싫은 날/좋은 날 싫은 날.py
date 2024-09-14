n, mood = map(int, input().split()) # 0 good 1 bad
percents = list(map(float, input().split()))
# good-good / good-bad / bad-good / bad-bad
# after n days
'''
good = good-good + bad-good
bad = bad-bad + good-bad
'''
good = bad = 0.0
if mood == 0:
    good = 1.0
else:
    bad = 1.0

for i in range(n):
    prev = good
    good = prev * percents[0] + bad * percents[2]
    bad = prev * percents[1] + bad * percents[3]

print(int(good*1000))
print(int(bad*1000))