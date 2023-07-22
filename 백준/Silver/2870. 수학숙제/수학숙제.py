digits = []
n = int(input())
for i in range(n):
    c = 0
    line = list(input())
    j = 0
    while j < len(line):
        num = []
        if line[j].isalpha():
            j += 1
            continue
        else:
            for k in range(j, len(line)):
                num.append(line[k])
                c = k + 1
                if c == len(line) or line[c].isalpha(): break
            number_str = "".join(num)
            digits.append(int(number_str))
            j = c
            del num
                

digits.sort()
for i in digits:
    print(i)