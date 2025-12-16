def solution(sizes):
    answer = 0
    for s in sizes: s.sort()
    sizes.sort(key=lambda x: x[0])
    maxN = sizes[-1][0]
    sizes.sort(key=lambda x: x[1])
    maxM = sizes[-1][1]
    answer = maxN * maxM
    return answer