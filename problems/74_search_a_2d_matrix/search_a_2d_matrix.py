from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        TARGET_ROW = -1
        while top <= bot:
            verticalMiddle = (bot + top) // 2
            if (
                matrix[verticalMiddle][0] == target
                or matrix[verticalMiddle][-1] == target
            ):
                return True
            if target < matrix[verticalMiddle][0]:
                bot = verticalMiddle - 1
            elif target > matrix[verticalMiddle][-1]:
                top = verticalMiddle + 1
            else:
                TARGET_ROW = verticalMiddle
                break

        left, right = 0, COLS - 1
        while left <= right:
            middle = (left + right) // 2
            if target < matrix[TARGET_ROW][middle]:
                right = middle - 1
            elif target > matrix[TARGET_ROW][middle]:
                left = middle + 1
            else:
                return True

        return False


solution = Solution()
# print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0))
print(
    solution.searchMatrix(
        [
            [-8, -7, -5, -3, -3, -1, 1],
            [2, 2, 2, 3, 3, 5, 7],
            [8, 9, 11, 11, 13, 15, 17],
            [18, 18, 18, 20, 20, 20, 21],
            [23, 24, 26, 26, 26, 27, 27],
            [28, 29, 29, 30, 32, 32, 34],
        ],
        -5,
    )
)
