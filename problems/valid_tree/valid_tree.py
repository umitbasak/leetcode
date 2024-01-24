from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                # since the graph is undirected, the other way of the previous edge is skipped
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        # "len(visit) == n" means that the graph is completely connected
        # "dfs(0,-1) == true" means that there are no cycles in the graph
        return dfs(0, -1) and len(visit) == n


solution = Solution()
# solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
# solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
