n = int(input())
pattern = input()
file_names = []
for i in range(n):
    file_names.append(input())

def read_pattern(pattern):
    index = pattern.index('*')
    start = pattern[0:index]
    end = pattern[index+1:]
    return start, end

def check_pattern(pattern, s):
    start, end = read_pattern(pattern)
    flag = False
    if len(start) + len(end) > len(s):
        return 'NE'
    if s[0:len(start)] == start:
        if s[len(s)-len(end):] == end:
            flag = True
    if flag: return 'DA'
    else: return 'NE'

for i in range(n):
    print(check_pattern(pattern, file_names[i]))