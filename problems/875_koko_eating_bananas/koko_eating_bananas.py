import math
from typing import List


class Solution:
    def howManyHoursToEat(self, piles: List[int], eatingSpeed: int) -> int:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / eatingSpeed)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        minEatingSpeed = right
        while left <= right:
            middle = (left + right) // 2
            if self.howManyHoursToEat(piles, middle) <= h:
                minEatingSpeed = min(minEatingSpeed, middle)
                right = middle - 1
            else:
                left = middle + 1

        return minEatingSpeed


solution = Solution()
# solution.minEatingSpeed([3, 6, 7, 11], 8)
# solution.minEatingSpeed([30, 11, 23, 4, 20], 5)
print(solution.minEatingSpeed([312884470], 312884469))
