N = int(input())
cases = [list(map(int, input().split())) for _ in range(N)]

def findFin(n, m):
    str_n = str(n)
    init_fin = int(str_n[-1])
    fin_num = 1
    for i in range(m):
        fin_num *= init_fin
        str_finNum = str(fin_num)
        fin_num = int(str_finNum[-1])
    if fin_num == 0:
        return 10
    else: return fin_num

for i in range(N):
    print(findFin(cases[i][0], cases[i][1]))