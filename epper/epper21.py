
# 1 요리가격
def cook_cos(ingredients, cost):
    answer = cost - sum(ingredients)
    return answer

# 2 문자열 압축
def zip_string(src):
    res = []
    if src[0] == '1': res.append('1')
    start, end = 0, 1
    answer = 1
    while end < len(src):
        if src[start] == src[end]: answer += 1 
        else: 
            start = end
            res.append(chr(ord('A')-1+answer))
            answer = 1
        end += 1
    answer = ''.join(res)
    return answer

# 3 프린터큐
def printer_queue(N, M, numbers):
    queue = []
    answer = 0
    for i in range(N):
        queue.append((i, numbers[i]))
    while True:
        x, y = queue.pop(0)
        if y == max(numbers): 
            answer += 1
            numbers[x] = 0
            if x == M: return answer
        else: queue.append((x,y))

# 4 개인정보수집 유효기간
def privacy_manage(today, terms, privacies):
    answer = []
    cy, cm, cd = list(map(int, today.split('.')))
    terms_dict = {}
    for t in terms:
        terms_dict[t[0]] = int(t[2:])
    for i in range(len(privacies)):
        dur, term = map(str, privacies[i].split())
        y, m, d = map(int, dur.split('.'))
        m += terms_dict[term]
        if m > 12: 
            y += m//12
            m %= 12   
        print(y, m, d)
        if y > cy: answer.append(i)
        elif y == cy and m > cm: answer.append(i)
        elif y == cy and m == cm and d <= cd: answer.append(i)
        
    return answer

    
print(privacy_manage("2020.01.01", ["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))


    
    
            
            
