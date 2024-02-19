class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def recurse(text1: str, i1, text2: str, i2) -> int:
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            if text1 == "" or text2 == "":
                return 0
            if text1[0] == text2[0]:
                return 1 + recurse(text1[1:], i1 + 1, text2[1:], i2 + 1)
            lcs = max(
                recurse(text1[1:], i1 + 1, text2, i2),
                recurse(text1, i1, text2[1:], i2 + 1),
            )
            dp[(i1, i2)] = lcs
            return lcs

        return recurse(text1, 0, text2, 0)


solution = Solution()
print(solution.longestCommonSubsequence("abcde", "ace"))
