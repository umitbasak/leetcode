from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle

            # left sorted portion
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            # right sorted portion
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1


solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 4))
# solution.search([1, 2, 3, 4, 5, 6], 4)
