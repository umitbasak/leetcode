from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets (the power set) of the given list of numbers.

        This function uses depth-first search (DFS) recursion to explore all decisions on
        whether to include each number in the current subset being built.
        """
        res = []  # This list will hold all the subsets generated.
        subset = []  # This list holds the current subset.

        def dfs(i: int):
            """
            Recursively explore each decision of including or not including nums[i].

            Args:
                i (int): The current index in nums we are considering.
            """
            # Base case: if we've considered all elements, add a copy of the current subset.
            if i >= len(nums):
                res.append(subset.copy())
                return

            # First decision: INCLUDE nums[i] in the subset.
            subset.append(nums[i])
            dfs(i + 1)  # Explore further with the current number included.

            # BACKTRACK: Remove the last number to try the alternative decision.
            subset.pop()

            # Second decision: EXCLUDE nums[i] from the subset.
            dfs(i + 1)  # Explore further without the current number.

        # Start the DFS recursion from index 0.
        dfs(0)
        return res


# Example usage (for testing purposes)
if __name__ == "__main__":
    sol = Solution()
    # Test case: generate all subsets of [1, 2, 3]
    print(sol.subsets([1, 2, 3]))
