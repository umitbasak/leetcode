import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        for i in range(len(points)):
            heapq.heappush(h, [self.calculateDistanceToOrigin(points[i]), i])

        solution = []
        for i in range(k):
            solution.append(points[heapq.heappop(h)[1]])
        return solution

    def calculateDistanceToOrigin(self, point: List[int]) -> int:
        return math.sqrt(point[0] * point[0] + point[1] * point[1])
