n = int(input())
strings = ['_' for i in range(n)]
for i in range(n):
    strings[i] = input()
for i in range(n):
    print(strings[i][0]+strings[i][len(strings[i])-1])