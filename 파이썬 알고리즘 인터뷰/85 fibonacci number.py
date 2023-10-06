import collections


class Solution:
    def fib1(self, n: int) -> int:
        fb = []

        def dp(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fb[n - 1] + fb[n-2]

        for i in range(n+1):
            fb.append(dp(i))

        return fb[n]

    dp = collections.defaultdict(int)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]

solution = Solution()
print(solution.fib(3))
print(solution.fib(4))

