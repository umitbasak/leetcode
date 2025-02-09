from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize the dp array to store the longest increasing subsequence starting at each index.
        # Each element is at least a subsequence of itself, so initialize with 1.
        dp = [1] * len(nums)

        # Iterate backwards through the list.
        # For each element, we want to check for any possible increasing sequence ahead.
        for i in range(len(nums) - 1, -1, -1):
            # Check every element after the current element.
            for j in range(i + 1, len(nums)):
                # If the current element is less than a future element, it could be part of an increasing sequence.
                if nums[i] < nums[j]:
                    # Update dp[i] to be the maximum between its current value and 1 plus the length of the subsequence starting from j.
                    dp[i] = max(dp[i], 1 + dp[j])

        # Return the maximum value from dp. This represents the length of the longest increasing subsequence in the list.
        return max(dp)


# Example usage:
solution = Solution()
# Test with the first example list.
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# Uncomment the line below to test with another example list.
# print(solution.lengthOfLIS([4, 10, 4, 3, 8, 9]))
