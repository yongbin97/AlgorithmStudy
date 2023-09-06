def solution(nums):
    return min(len(nums)//2, len(set(nums)))

# N 중 -> N/2 가져감
# 가장 많은 종류 가져가기