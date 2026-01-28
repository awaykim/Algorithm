"""
2개의 상의를 사용해 나올 수 있는 경우의 수는 안 입는거까지 포함하여 3가지 입니다. 2개의 하의를 사용해 나올 수 있는 경우의 수도 마찬가지로 3가지 입니다. 상의를 하나 골랐다면 그 다음에는 하의를 하나 골라야 합니다. 상의 중 하나, 3가지 중 택 1, 하의 중 하나 3가지 중 택 1. 3 * 3이 되고 최소 한개 이상의 옷을 입는다 하였으니 둘 다 안 입는 것을 제외하면 8이 됩니다.
"""
def solution(clothes):
    c_map = {}
    for c in clothes:
        key = c[1]
        if key in c_map.keys():
            c_map[key] += 1
        else: 
            c_map.update({ key: 1 })
    
    answer = 1
    for cnt in c_map.values():
        answer *= cnt + 1

    return answer - 1
