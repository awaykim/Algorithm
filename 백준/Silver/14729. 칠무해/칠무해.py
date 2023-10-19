# 14729
n = int(input())
seven = []
for _ in range(n):
    grade = float(input())
    if len(seven) < 7: 
        seven.append(grade)
        seven.sort()
    else:
        if grade < seven[-1]:
            seven.pop(-1)
            seven.append(grade) 
            seven.sort()
for i in range(7): print('{:.3f}'.format(seven[i]))