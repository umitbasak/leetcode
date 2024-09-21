from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        validParantheses = []

        def recursiveUtil(leftParantheses, rightParantheses, currentString):
            if rightParantheses == n:
                validParantheses.append(currentString)
                return
            if leftParantheses > rightParantheses:
                recursiveUtil(
                    leftParantheses, rightParantheses + 1, currentString + ")"
                )
            if leftParantheses < n:
                recursiveUtil(
                    leftParantheses + 1, rightParantheses, currentString + "("
                )

        recursiveUtil(0, 0, "")
        return validParantheses


solution = Solution()
print(solution.generateParentheses(3))
