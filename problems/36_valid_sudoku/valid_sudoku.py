import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                currentElement = board[r][c]
                if currentElement == ".":
                    continue
                if (
                    currentElement in rows[r]
                    or currentElement in cols[c]
                    or currentElement in squares[r // 3, c // 3]
                ):
                    return False
                rows[r].add(currentElement)
                cols[c].add(currentElement)
                squares[r // 3, c // 3].add(currentElement)

        return True
