from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for prerequisite in prerequisites:
            if (
                prerequisite[0] in graph
                and prerequisite[1] not in graph[prerequisite[0]]
            ):
                graph[prerequisite[0]].append(prerequisite[1])
            else:
                graph[prerequisite[0]] = [prerequisite[1]]

        canComplete = set()

        def dfs(number, preqs, currentlyVisited):
            if number in currentlyVisited:
                return False
            if number in canComplete:
                return True
            if preqs == []:
                canComplete.add(number)
                return True
            currentlyVisited.add(number)
            for preq in preqs:
                if preq in currentlyVisited:
                    continue
                if dfs(preq, graph[preq], currentlyVisited):
                    canComplete.add(preq)
                    return True

        for number, preqs in graph.items():
            if not dfs(number, preqs, set()):
                return False

        return True


solution = Solution()
# print(solution.canFinish(2, [[0, 1]]))
# print(solution.canFinish(3, [[1, 0], [1, 2], [0, 1]]))
print(solution.canFinish(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]))
