from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zeroLocs = []

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeroLocs.append((r, c))

        def zeroCol(matrix, col):
            for row in range(ROWS):
                matrix[row][col] = 0

        def zeroRow(matrix, row):
            for col in range(COLS):
                matrix[row][col] = 0

        for loc in zeroLocs:
            zeroRow(matrix, loc[0])
            zeroCol(matrix, loc[1])

        return matrix
