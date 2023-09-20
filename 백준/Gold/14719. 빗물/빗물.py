h, w = map(int, input().split())
blocks = list(map(int, input().split()))
standard = (0, blocks[0])
amount = 0
for i in range(1, w):
    point, top = standard
    if top == max(blocks[point:]) and point != w-1:
        p = point
        standard = (w-1, blocks[-1])
        for i in range(w-1, p, -1):
            point, top = standard
            if blocks[i] < top:  
                    amount += top - blocks[i]
            else:
                standard = (i, blocks[i])
        break
    else:
        if blocks[i] < top:  
            amount += top - blocks[i]
        else:
            standard = (i, blocks[i])
print(amount)