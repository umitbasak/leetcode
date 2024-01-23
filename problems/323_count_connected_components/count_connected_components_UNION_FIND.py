from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(n1):
            if par[n1] == n1:
                return n1
            par[n1] = par[par[n1]]  # path compression
            return find(par[n1])

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)  # find root parents

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


solution = Solution()
# print(solution.countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]))
print(solution.countComponents(6, [[0, 1], [2, 3], [4, 5], [1, 2], [3, 4]]))
