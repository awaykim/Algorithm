n = int(input())
m = int(input())
materials = list(map(int, input().split()))
count = 0

while True:
    i = materials.pop(0)
    remain = m - i
    if remain in materials:
        materials.remove(remain)
        count = count + 1
    if len(materials) < 2 : break

print(count)