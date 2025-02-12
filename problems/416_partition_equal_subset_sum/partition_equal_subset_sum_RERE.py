from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Find the number of elements and the total sum of all values.
        size = len(nums)
        total = sum(nums)

        # If the total sum is odd, it's impossible to split into two equal subsets.
        if total % 2:
            return False

        # The target sum each subset needs to achieve.
        target = total // 2

        # The set dp holds all possible subset sums we've seen so far.
        dp = set()
        dp.add(0)  # Start with a subset sum of 0 (i.e., no elements).

        # Loop through the indices of nums in reverse order.
        for i in range(size - 1, -1, -1):
            # A new set to hold updated subset sums including the current number.
            nextDP = set()
            for t in dp:
                # Always consider the current subset sum without adding the new value.
                nextDP.add(t)
                # If adding the current number equals the target, partition is possible.
                if t + nums[i] == target:
                    return True
                # If the sum exceeds the target, skip adding this number.
                elif t + nums[i] > target:
                    continue
                # Otherwise, add the new subset sum including the current number.
                nextDP.add(t + nums[i])
            # Replace dp with the newly updated set of subset sums.
            dp = nextDP

        # If no subset sum equals the target, partitioning into two equal subsets is impossible.
        return False


# Testing the solution with an example list
solution = Solution()
print(
    solution.canPartition([1, 5, 5, 11])
)  # Expected: True because partition [11] and [1,5,5] have the same sum

# Uncomment the line below to test with another example
# print(solution.canPartition([1, 1, 2, 2]))
