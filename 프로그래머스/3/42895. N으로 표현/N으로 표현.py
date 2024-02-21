def solution(N, number):
    answer = -1
    dp = []
    for cnt in range(1, 9):
        cases = set()
        cases.add(int(str(N) * cnt))
        for i in range(cnt-1):
            for op1 in dp[i]:
                for op2 in dp[-i-1]:
                    cases.add(op1 + op2)
                    cases.add(op1 - op2)
                    cases.add(op1 * op2)
                    if op2 != 0:
                        cases.add(op1 // op2)
        if number in cases:
            answer = cnt
            break
        dp.append(cases)

    return answer