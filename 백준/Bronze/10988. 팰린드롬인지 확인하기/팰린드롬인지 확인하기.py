word = input()
rev_word = "".join(reversed(word))
if rev_word == word:
    print(1)
else: print(0)