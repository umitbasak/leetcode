from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []
        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i + 1)

            # For eliminating duplicates, as long as the nums[i+1] is equal to nums[i]
            # shift the index, since the other possible permutations have already been
            # calculated with the recursive calls above
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            cur.pop()
            backtrack(i + 1)

        backtrack(0)

        return res
