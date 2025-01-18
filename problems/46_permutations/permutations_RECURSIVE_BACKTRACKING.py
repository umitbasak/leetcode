from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res, cur = [], []

        def backtrack():
            if len(cur) == n:
                res.append(cur.copy())
                return

            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack()
                    cur.pop()

        backtrack()
        return res
