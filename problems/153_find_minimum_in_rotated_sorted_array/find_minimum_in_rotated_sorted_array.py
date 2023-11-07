from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            middle = (right + left) // 2
            res = min(res, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return res


solution = Solution()
# print(solution.findMin([3, 4, 5, 1, 2]))
print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))
