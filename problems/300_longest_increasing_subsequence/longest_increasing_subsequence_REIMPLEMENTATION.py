from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


# Example usage:
solution = Solution()
# Test with the first example list.
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# Uncomment the line below to test with another example list.
# print(solution.lengthOfLIS([4, 10, 4, 3, 8, 9]))
