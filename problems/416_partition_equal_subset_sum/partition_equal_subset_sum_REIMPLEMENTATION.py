from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # If the total sum is odd, it's impossible to split into two equal subsets.
        if sum(nums) % 2:
            return False

        # dp will hold all possible subset sums encountered so far.
        dp = set()
        dp.add(0)

        # The target is half of the total sum, which is what each subset should sum to.
        target = sum(nums) // 2

        # Process elements in reverse order.
        for i in range(len(nums) - 1, -1, -1):
            nextDP = (
                set()
            )  # Will hold the new set of subset sums including the current number.
            for t in dp:
                # If adding the current number results in the target sum, a valid partition exists.
                if (t + nums[i]) == target:
                    return True
                # Add the new sum (with the current number) to nextDP.
                nextDP.add(t + nums[i])
                # Also carry over the existing sum without the current number.
                nextDP.add(t)
            # Update dp with the new subset sums.
            dp = nextDP
        # If no subset sum equals the target, partition is not possible.
        return False


# Testing the solution with an example list
solution = Solution()
print(
    solution.canPartition([1, 5, 5, 11])
)  # Expected: True because partition [11] and [1,5,5] have the same sum

# Uncomment the line below to test with another example
# print(solution.canPartition([1, 1, 2, 2]))
