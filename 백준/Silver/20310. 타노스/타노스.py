import sys
s = sys.stdin.readline()
new_s = '0' * (s.count('0') // 2) + '1' * (s.count('1') // 2)
print(new_s)