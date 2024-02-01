def solution(today, terms, privacies):
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
        if m == 0: 
            m = 12
            y -= 1
        if y < cy: answer.append(i+1)
        elif y == cy and m < cm: answer.append(i+1)
        elif y == cy and m == cm and d <= cd: answer.append(i+1)
        
    return answer