from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0

        intervals.sort(key=lambda i: (i[0], i[1]))

        extracted = 0
        i = 1
        while i < len(intervals):
            if intervals[i - 1][1] <= intervals[i][0]:
                i += 1
            else:
                if intervals[i][1] < intervals[i - 1][1]:
                    intervals.pop(i - 1)
                else:
                    intervals.pop(i)
                extracted += 1

        return extracted


solution = Solution()
# test1 = solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
# print(test1)

test2 = solution.eraseOverlapIntervals(
    [
        [-52, 31],
        [-73, -26],
        [82, 97],
        [-65, -11],
        [-62, -49],
        [95, 99],
        [58, 95],
        [-31, 49],
        [66, 98],
        [-63, 2],
        [30, 47],
        [-40, -26],
    ]
)
print(test2)
