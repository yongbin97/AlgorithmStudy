from typing import List, Optional


class Solution:
    @staticmethod
    def strip_by_zero(height: List[int]) -> Optional[List[int]]:
        left = 0
        right = len(height) - 1
        while height[left] == 0 or height[right] == 0:
            if left == right:
                return None
            if height[left] == 0:
                left += 1
            if height[right] == 0:
                right -= 1
        return height[left: right + 1]

    def trap(self, height: List[int]) -> int:
        max_h = max(height)
        water = 0
        for _ in range(max_h):
            height = self.strip_by_zero(height)
            water += height.count(0)
            height = [h-1 if h else h for h in height]
        return water


height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height2 = [4, 2, 0, 3, 2, 5]
solution = Solution()
print(solution.trap(height1))
print(solution.trap(height2))
