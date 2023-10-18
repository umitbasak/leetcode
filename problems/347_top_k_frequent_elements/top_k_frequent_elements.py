from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(list)
        res = []

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for _ in range(k):
            max_key = max(frequency, key=frequency.get)
            res.append(max_key)
            frequency.pop(max_key)

        return res


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
