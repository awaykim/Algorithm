n = int(input())

words = [[] for _ in range(51)]

for _ in range(n):
    word = input()
    if word in words[len(word)]: continue
    words[len(word)].append(word)

for i in range(51):
    words[i].sort()
    for j in range(len(words[i])):
        print(words[i][j])