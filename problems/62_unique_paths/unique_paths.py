class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]

        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]

        return dp[0][0]


solution = Solution()
test1 = solution.uniquePaths(3, 7)
