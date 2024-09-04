from math import trunc
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip("-+").isnumeric():
                stack.append(int(token))
            else:
                previousNum = stack.pop()
                previousNum2 = stack.pop()
                match token:
                    case "+":
                        stack.append(previousNum2 + previousNum)
                    case "-":
                        stack.append(previousNum2 - previousNum)
                    case "*":
                        stack.append(previousNum2 * previousNum)
                    case "/":
                        stack.append(trunc(previousNum2 / previousNum))

        return stack[0]


solution = Solution()
# tokens = ["4", "13", "5", "/", "+"]
# solution.evalRPN(tokens)
tokens2 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
solution.evalRPN(tokens2)
