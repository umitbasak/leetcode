from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1

        maxArea = 0

        while left < right:
            currentArea = (right - left) * min(height[left], height[right])
            maxArea = max(currentArea, maxArea)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxArea


solution = Solution()
print(solution.maxArea([2, 3, 10, 5, 7, 8, 9]))
