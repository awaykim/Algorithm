name = list(map(str, input()))
vector = [0] * 26
for i in range(26): vector[i] = name.count(chr(ord('A')+i))
string = ''
mid = ''
for i in range(26):
    if vector[i] == 0: continue
    if vector[i] % 2 != 0:
        if len(name) % 2 == 0: 
            print('I\'m Sorry Hansoo')
            exit()
        else:
            if mid =='': mid = chr(ord('A')+i)
            else:
                print('I\'m Sorry Hansoo')
                exit()
    string = string + chr(ord('A')+i) * (vector[i] // 2)
ans = string + mid + string[::-1]
print(ans)