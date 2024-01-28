from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if len(intervals) < 2:
            return intervals

        i = 1
        while i < len(intervals):
            preStart, preEnd = intervals[i - 1][0], intervals[i - 1][1]
            curStart, curEnd = intervals[i][0], intervals[i][1]

            if preEnd < curStart:
                i += 1
                continue
            else:
                intervals[i] = [min(preStart, curStart), max(preEnd, curEnd)]
                intervals.pop(i - 1)

        return intervals


solution = Solution()
# test1 = solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
# print(test1)
test2 = solution.merge([[1, 4], [0, 0]])
print(test2)
