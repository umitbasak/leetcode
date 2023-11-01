from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            firstNum = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                secondNum = nums[left]
                thirdNum = nums[right]
                sum = firstNum + secondNum + thirdNum

                if sum == 0:
                    result.append([firstNum, secondNum, thirdNum])
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1

        return result


solution = Solution()
# print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([0, 0, 0, 0]))
# -4, -1, -1, 0, 1, 2
