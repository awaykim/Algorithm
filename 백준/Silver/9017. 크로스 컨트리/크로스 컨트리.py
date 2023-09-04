import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    passed = []
    for i in range(1, max(data)+1):
        if data.count(i) > 5: passed.append(i)
    # total score, score of 5th, count
    table = [[0, 0, 0] for i in range(max(data) + 1)]
    # team, total, 5th
    ans = [0, sys.maxsize, sys.maxsize]
    score = 0
    for i in range(len(data)):
        team = data[i]
        if team not in passed: continue
        table[team][2] += 1
        score += 1
        if table[team][2] == 5: table[team][1] = score
        elif table[team][2] < 5: table[team][0] += score
    for i in range(1, len(table)):
        if table[i][2] < 6: continue
        if table[i][0] < ans[1]: 
            ans[0], ans[1], ans[2] = i, table[i][0], table[i][1]
        elif table[i][0] == ans[1] and table[i][1] < ans[2]:
            ans[0], ans[1], ans[2] = i, table[i][0], table[i][1]
    print(ans[0])