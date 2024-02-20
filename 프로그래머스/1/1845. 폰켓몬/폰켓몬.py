def solution(nums):
    category = set(nums)
    answer = min(len(category), len(nums)//2)
    return answer