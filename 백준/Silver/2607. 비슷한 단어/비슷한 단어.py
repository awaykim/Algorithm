import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(n)]
def solution(n, data):
    s = data[0]
    s_dic = dict()
    for _ in set(s): s_dic[_] = s.count(_)

    def check(t):
        flag = False
        if abs(len(t)-len(s)) > 1: return False
        union = set(s) | set(t)
        tmp = set()
        for i in union:
            if flag: break
            tmp.add(i)
            if t.count(i) == s.count(i): pass
            else:
                if t.count(i) - s.count(i) == 1:
                    t.remove(i)
                    for j in union - tmp:
                        if s.count(j) - t.count(j) == 1:
                            t.append(j)
                            flag = True
                            break
                elif s.count(i) - t.count(i) == 1:
                    t.append(i)
                    for j in union - tmp:
                        if t.count(j) - s.count(j) == 1:
                            t.remove(j)
                            flag = True
                            break
                else: break
        t_dic = {}
        for _ in set(t): t_dic[_] = t.count(_)     
        if s_dic == t_dic: return True
        else: return False       
            



    table = []
    for i in range(1, n):
        # print(data[i], check(data[i]))
        table.append(check(list(data[i])))
    return table.count(True)


print(solution(n, data))