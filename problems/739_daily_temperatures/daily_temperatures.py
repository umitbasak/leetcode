from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []  # pair: [index, temp]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                resIndex, resTemp = stack.pop()
                result[resIndex] = i - resIndex
            stack.append([i, t])

        return result


solution = Solution()
solution.dailyTemperatures([1, 2, 3, 2, 1])
