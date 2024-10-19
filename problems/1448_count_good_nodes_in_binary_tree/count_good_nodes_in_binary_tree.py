import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        goodNodes = set()

        def dfs(curNode: TreeNode, maxValInCurrentLane: int):
            if not curNode:
                return

            if curNode.val >= maxValInCurrentLane:
                maxValInCurrentLane = curNode.val
                print(curNode.val)
                if curNode not in goodNodes:
                    goodNodes.add(curNode)

            dfs(curNode.left, maxValInCurrentLane)
            dfs(curNode.right, maxValInCurrentLane)

        dfs(root, -math.inf)
        return len(goodNodes)
