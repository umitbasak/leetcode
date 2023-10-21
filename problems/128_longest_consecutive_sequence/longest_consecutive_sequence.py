from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def findSequenceOfCharacter(numsSet: set, num):
            sequence = 0
            leftNum = num
            while leftNum in numsSet:
                numsSet.remove(leftNum)
                sequence += 1
                leftNum -= 1
            rightNum = num + 1
            while rightNum in numsSet:
                numsSet.remove(rightNum)
                sequence += 1
                rightNum += 1

            return sequence

        numsSet = set(nums)

        longestSequence = 0

        for num in nums:
            longestSequence = max(
                findSequenceOfCharacter(numsSet, num), longestSequence
            )

        return longestSequence
