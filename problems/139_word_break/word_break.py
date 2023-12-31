from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        currentWord = ""

        for c in s:
            currentWord += c
            if currentWord in wordSet:
                currentWord = ""
        if currentWord == "":
            return True
        else:
            return False


solution = Solution()
# solution.wordBreak("leetcode", ["leet", "code"])
solution.wordBreak("aaaaaaa", ["aaaa", "aaa"])
