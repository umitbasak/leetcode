from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total > target or i >= len(candidates):
                return
            if total == target:
                res.append(cur.copy())
                return

            # include the value at the current index
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            # do not include the value at the current index
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
