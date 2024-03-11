name = list(map(str, input()))
vector = [0] * 26
for i in range(26): vector[i] = name.count(chr(ord('A')+i))
string = ''
mid = ''
for i in range(26):
    if vector[i] % 2 == 1:
        if mid != '':
            print('I\'m Sorry Hansoo')
            exit()
        mid = chr(ord('A')+i)
    string += chr(ord('A')+i) * (vector[i] // 2)
ans = string + mid + string[::-1]
print(ans)