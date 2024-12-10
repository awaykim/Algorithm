def solution(friends, gifts):
    answer = 0
    exchanges = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    points = [0 for _ in range(len(friends))]
    cnts = [0 for _ in range(len(friends))]
    
    for gift in gifts:
        g, r = gift.split(" ")
        g_idx = friends.index(g)
        r_idx = friends.index(r)
        exchanges[g_idx][r_idx] += 1
        points[g_idx] += 1
        points[r_idx] -= 1
        
    for i in range(len(friends)-1):
        for j in range(i+1, len(friends)):
            if exchanges[i][j] > exchanges[j][i]:
                cnts[i] += 1
            elif exchanges[i][j] == exchanges[j][i]:
                if points[i] > points[j]:
                    cnts[i] += 1
                elif points[i] < points[j]:
                    cnts[j] += 1
                else:
                    continue
            else:
                cnts[j] += 1
    answer = max(cnts)
    return answer