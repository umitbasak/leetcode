from typing import List

# TODO solve the problem that arises when we encounter duplicate values in the
# result array


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            # in order to omit duplicate elements we create a set to keep track
            numSet = set()

            firstNum = nums[i]

            numSet.add(firstNum)

            left = i + 1
            right = n - 1

            while left < right:
                # if (
                #     nums[left] in numSet
                #     or nums[right] in numSet
                #     or nums[left] == nums[right]
                # ):
                #     continue
                if nums[left] in numSet:
                    left += 1
                    continue
                elif nums[right] in numSet:
                    right -= 1
                    continue
                elif nums[left] == nums[right]:
                    left += 1
                    right -= 1
                    continue
                sum = firstNum + nums[left] + nums[right]
                if sum == 0:
                    result.append([firstNum, nums[left], nums[right]])
                    break
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    raise Exception("Something unexpected happened")

        return result


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
