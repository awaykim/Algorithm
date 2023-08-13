num_li = list(map(int, str(input())))
num_li.sort(reverse=True)
for i in num_li:
    print(i,end='')