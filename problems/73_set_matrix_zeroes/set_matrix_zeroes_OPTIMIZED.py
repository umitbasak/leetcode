from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zeroRows = set()
        zeroCols = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)

        def zeroCol(matrix, col):
            for row in range(ROWS):
                matrix[row][col] = 0

        def zeroRow(matrix, row):
            for col in range(COLS):
                matrix[row][col] = 0

        for row in zeroRows:
            zeroRow(matrix, row)

        for col in zeroCols:
            zeroCol(matrix, col)

        return matrix
