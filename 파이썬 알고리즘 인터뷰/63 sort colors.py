from typing import List


class Solution:
    def sortColors2(self, nums: List[int]) -> None:
        for idx in range(len(nums)):
            curr = idx
            while curr > 0 and nums[curr] < nums[curr-1]:
                nums[curr], nums[curr-1] = nums[curr-1], nums[curr]
                curr -= 1

    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            # red
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1

            # blue
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]

            else:
                white += 1

            print(nums)


solution = Solution()
solution.sortColors([2,0,2,1,1,0])
solution.sortColors([2,0,1])

