n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
sg = list(map(int, input().split()))
res = []
# 딕셔너리 or 배열
sg_dict = {}
for num in numbers:
    if num in sg_dict: sg_dict[num] += 1
    else: sg_dict[num] = 1
for s in sg:
    if s in sg_dict: print(sg_dict[s], end=' ')
    else: print(0, end=' ')