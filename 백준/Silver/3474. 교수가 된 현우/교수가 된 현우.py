t = int(input())
for _ in range(t):
    case = int(input())
    fives = []
    for i in range(1, case):
        five = case // (5 ** i)
        if not five: break
        fives.append(five)
    print(sum(fives))