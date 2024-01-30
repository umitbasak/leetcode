from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return str(self.start) + ", " + str(self.end)


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda x: (x.start, x.end))
        days = [[intervals[0]]]
        for i in range(1, len(intervals)):
            added = False
            for day in days:
                if day[-1].end <= intervals[i].start:
                    day.append(intervals[i])
                    added = True
                    break
            # conflict
            if not added:
                days.append([intervals[i]])

        return len(days)


solution = Solution()

# int1 = Interval(0, 40)
# int2 = Interval(5, 10)
# int3 = Interval(15, 20)
# test1 = solution.minMeetingRooms([int1, int2, int3])
test2 = solution.minMeetingRooms(
    [Interval(1, 5), Interval(5, 10), Interval(10, 15), Interval(15, 20)]
)

print(test2)
