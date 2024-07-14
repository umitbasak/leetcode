import math


class StackNode:
    def __init__(self, value, minAtPoint) -> None:
        self.value = value
        self.minAtPoint = minAtPoint


class MinStack:
    def __init__(self):
        self.minStack = []
        self.currentMin = math.inf

    def push(self, val: int) -> None:
        self.minStack.append(StackNode(val, self.currentMin))
        if val < self.currentMin:
            self.currentMin = val

    def pop(self) -> None:
        poppedNode = self.minStack.pop()
        self.currentMin = poppedNode.minAtPoint

    def top(self) -> int:
        return self.minStack[len(self.minStack) - 1].value

    def getMin(self) -> int:
        return self.currentMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
