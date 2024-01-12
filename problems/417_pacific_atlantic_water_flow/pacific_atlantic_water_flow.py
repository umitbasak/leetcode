import math
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        canFlowPacific = set()
        canFlowAtlantic = set()
        result = []

        def dfs(r, c, prevHeight, originR, originC):
            print(r, c)
            if r >= ROWS or c >= COLS:
                canFlowAtlantic.add((originR, originC))
                return True
            if r < 0 or c < 0:
                canFlowPacific.add((originR, originC))
                return True
            if heights[r][c] > prevHeight:
                return False

            dfs(r + 1, c, heights[r][c], originR, originC)
            dfs(r - 1, c, heights[r][c], originR, originC)
            dfs(r, c + 1, heights[r][c], originR, originC)
            dfs(r, c - 1, heights[r][c], originR, originC)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, math.inf, r, c)

        for nodeTuple in canFlowPacific:
            if nodeTuple in canFlowPacific:
                result.append(nodeTuple)

        return result


solution = Solution()
# print(solution.pacificAtlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
print(
    solution.pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
)
