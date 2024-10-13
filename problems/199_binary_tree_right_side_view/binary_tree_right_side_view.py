import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# A breadth first search algorithm will be employed on this problem. The rightmost node of each level will
# be stored inside an array which will be returned at the end of the execution


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque([root])

        while queue:
            rightSide = None
            levelLength = len(
                queue
            )  # find the length of the level in order to only pop the nodes which are on that level

            # pop every node in the current level and add their left and right children respectively
            for i in range(levelLength):
                node = queue.popleft()

                # if the popped node is None nothing will be done
                if node:
                    rightSide = node  # update rightSide variable so that at the end of the loop this variable will be the rightmost of that level
                    queue.append(node.left)
                    queue.append(node.right)

            if rightSide:
                res.append(rightSide.val)

        return res
