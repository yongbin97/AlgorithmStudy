from collections import defaultdict


class Solution:
    dp = defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]

    def climbStairs2(self, n: int) -> int:
        factorial_dict = defaultdict(int)

        def factorial(x):
            if x <= 1:
                return 1
            elif x not in factorial_dict.keys():
                factorial_dict[x] = x * factorial(x - 1)
            return factorial_dict[x]

        # n = 2 * a + 1 * b
        a, b = n // 2, n % 2
        answer = 0
        while a >= 0:
            answer += factorial(a + b) // (factorial(a) * factorial(b))
            a -= 1
            b += 2
        return answer


solution = Solution()
print(solution.climbStairs(3))
print(solution.climbStairs(2))
