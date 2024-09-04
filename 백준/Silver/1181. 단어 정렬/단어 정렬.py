n = int(input())
# words = [[] for _ in range(51)]
words = []
for _ in range(n):
    word = input()
    words.append(word)
# words.sort() 
# words.sort(key=len)
# words = sorted(words, key= lambda x : (len(x), x))
# res = []
res = list(set(words))
res = sorted(res, key= lambda x : (len(x), x))
for i in range(len(res)):
    print(res[i])