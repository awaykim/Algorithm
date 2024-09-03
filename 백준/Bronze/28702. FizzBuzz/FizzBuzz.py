a = input()
b = input()
c = input()
li = [a, b, c]
ans_num = 0
ans = ''
for i in range(len(li)):
    if li[i].isdigit(): 
        t = int(li[i])
        ans_num = t + 3 - i
        break


if ans_num % 3 == 0: ans = 'Fizz'
if ans_num % 5 == 0: ans += 'Buzz'

print(ans if ans else ans_num)