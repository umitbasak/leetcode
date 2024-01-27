from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # if new interval ends before the current interval starts
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # if the new interval starts after the current interval ends
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # if the new interval and current interval intersects,
            # the newInterval is updated so that it covers both itself and the current interval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        res.append(newInterval)
        return res


solution = Solution()
print(solution.insert([[1, 3], [6, 9]], [2, 5]))
