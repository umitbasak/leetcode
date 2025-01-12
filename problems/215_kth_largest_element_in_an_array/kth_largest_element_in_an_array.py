import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for num in nums:
            heapq.heappush(h, num * -1)

        solution = 0
        for i in range(k):
            solution = heapq.heappop(h) * -1

        return solution
