import sys
from typing import List


class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = prices[0]
        for price in prices:
            if min_value > price:
                min_value = price
            elif price > min_value:
                if price - min_value > max_profit:
                    max_profit = price - min_value

        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit

solution = Solution()
prices_1 = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices_1))

prices_2 = prices = [7,6,4,3,1]
print(solution.maxProfit(prices_2))