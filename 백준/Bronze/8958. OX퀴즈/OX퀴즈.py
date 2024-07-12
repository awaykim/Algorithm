T = int(input())
for t in range(T):
    quiz = list(input())
    score = 0
    var = 0
    while quiz:
        if quiz.pop() == 'O':
            var += 1
            score += var
        else:
            var = 0
    print(score)

        
    