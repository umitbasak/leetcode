from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjDict = {i: [] for i in range(n)}
        for edge in edges:
            adjDict[edge[0]].append(edge[1])
            adjDict[edge[1]].append(edge[0])

        isl = {i: [] for i in range(n)}
        islIndex = [0]
        visited = set()

        def dfs(node):
            # if the node is already visited return
            if node in visited:
                return
            # if the node is not visited, add this node as an element of the current island index
            isl[islIndex[0]].append(node)
            visited.add(node)
            for adjNode in adjDict[node]:
                dfs(adjNode)
            # islIndex[0] += 1
            return

        for i in range(n):
            dfs(i)
            islIndex[0] += 1

        islandCount = 0

        for key, value in isl.items():
            if value != []:
                islandCount += 1

        return islandCount


solution = Solution()
# print(solution.countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]))
print(solution.countComponents(3, [[0, 1], [0, 2]]))
