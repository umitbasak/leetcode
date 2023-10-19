from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        lenNums = len(nums)

        prefix = 1
        for i in range(lenNums):
            res.append(prefix)
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(lenNums - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res


solution = Solution()
solution.productExceptSelf([1, 2, 3, 4])
