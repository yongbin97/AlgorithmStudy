def solution(nums):
    pocketmon_dict = {}
    pick = len(nums) / 2
    
    for num in nums:
        if num not in pocketmon_dict.keys():
            pocketmon_dict[num] = 1
        else:
            pocketmon_dict[num] += 1
    
    return min(pick, len(pocketmon_dict))