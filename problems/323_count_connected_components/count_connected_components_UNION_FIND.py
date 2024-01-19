from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def countParents(parents):
            numSet = set()
            count = 0
            for n in parents:
                if n not in numSet:
                    numSet.add(n)
                    count += 1
            return count

        parents = [i for i in range(n)]
        ranks = [1 for i in range(n)]

        for edge in edges:
            parent0 = parents[edge[0]]
            parent1 = parents[edge[1]]

            if ranks[parent0] > ranks[parent1]:
                ranks[parent0] += ranks[parent1]
                ranks[parent1] = 0
                parents[edge[1]] = parent0
            else:
                ranks[parent1] += ranks[parent0]
                ranks[parent0] = 0
                parents[edge[0]] = parent1

        return countParents(parents)


solution = Solution()
# print(solution.countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]))
print(solution.countComponents(6, [[0, 1], [2, 3], [4, 5], [1, 2], [3, 4]]))
