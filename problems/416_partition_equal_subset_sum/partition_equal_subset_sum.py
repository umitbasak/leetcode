from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        sumSet = set([0, nums[-1]])
        if target in sumSet:
            return True

        for i in range(len(nums) - 2, -1, -1):
            for n in sumSet.copy():
                if n + nums[i] not in sumSet:
                    sumSet.add(n + nums[i])
                    if n + nums[i] == target:
                        return True


solution = Solution()
# solution.canPartition([1, 2, 3, 4])
solution.canPartition([1, 1])
