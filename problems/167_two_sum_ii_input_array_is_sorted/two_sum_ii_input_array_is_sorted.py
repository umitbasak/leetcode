from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        remainingValue = {}

        for i in range(len(numbers)):
            if numbers[i] in remainingValue:
                return [remainingValue[numbers[i]] + 1, i + 1]
            else:
                remainingValue[target - numbers[i]] = i

        return [-1]


solution = Solution()
# solution.twoSum([2, 7, 11, 15], 9)
solution.twoSum([-1, 0], -1)
