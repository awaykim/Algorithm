def solution(lottos, win_nums):
    same = len(set(lottos) & set(win_nums))
    print(same)
    low = 7 - same
    if not same: low = 6
    high = low - lottos.count(0)
    if not high: high = 1
    return [high, low]