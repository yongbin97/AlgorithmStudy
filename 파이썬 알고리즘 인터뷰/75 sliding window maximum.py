from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        max_v = nums[0]
        answer = []

        for idx, num in enumerate(nums):
            window.append(num)

            # set first window
            if idx < k - 1:
                if num >= max_v:
                    max_v = num
                continue

            # update max_v
            if max_v is None:
                max_v = num
                for i in range(k):
                    if nums[idx - i] > max_v:
                        max_v = nums[idx - i]

            elif num >= max_v:
                max_v = num

            answer.append(max_v)

            # pop max value, set max value
            if max_v == window.popleft():
                max_v = None

        return answer

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()

        for i, num in enumerate(nums):
            while window and window[0] < i - k + 1:
                window.popleft()

            while window and nums[window[-1]] < num:
                window.pop()

            window.append(i)
            if i >= k - 1:
                result.append(nums[window[0]])

        return result


solution = Solution()
print(solution.maxSlidingWindow(nums=[1, 3, -1, -3, 2, 5, 3, 6, 7], k=3))  # [3,3,2,5,5,6,7]
print(solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=8))  # [7]
print(solution.maxSlidingWindow(nums=[1, -1], k=1))  # [1,-1]
print(solution.maxSlidingWindow(nums=[9, 10, 9, -7, -4, -8, 2, -6], k=5))  # [1,-1]
