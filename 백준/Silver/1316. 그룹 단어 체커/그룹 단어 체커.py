n = int(input())
ans_cnt = 0
for _ in range(n):
    flag = True
    word = input()
    word_set = set(word)
    for w in word_set:
        w_cnt = word.count(w)
        if w * w_cnt not in word: 
            flag = False
            break
    if flag: ans_cnt += 1
print(ans_cnt)