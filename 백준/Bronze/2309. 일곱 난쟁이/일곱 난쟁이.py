# 2309
dwarf = [0] * 9
for i in range(9):
    dwarf[i] = int(input())
dwarf.sort(key=lambda x: x)
flag = False
for i in range(8):
    if flag: break
    for j in range(i + 1, 9):
        tmp1, tmp2 = dwarf[i], dwarf[j]
        if sum(dwarf) - (tmp1 + tmp2) == 100: 
            dwarf.remove(tmp1)
            dwarf.remove(tmp2)
            flag = True
            break
for i in dwarf: print(i)
