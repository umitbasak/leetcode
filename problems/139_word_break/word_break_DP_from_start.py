from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize a DP array where dp[i] represents whether s[:i] can be segmented into words from wordDict.
        dp = [False] * (len(s) + 1)
        # The empty substring is always "segmentable"
        dp[0] = True

        # Process the string from the beginning to the end
        for i in range(len(s)):
            # Only proceed if the substring s[:i] can be segmented
            if not dp[i]:
                continue
            # Try each word in the dictionary
            for w in wordDict:
                # Check if the current index i plus length of w doesn't exceed s, and if the substring matches w
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    # If it matches, mark dp[i+len(w)] as True indicating s[:i+len(w)] can be segmented
                    dp[i + len(w)] = True

        # Finally, return whether the whole string s can be segmented into dictionary words
        return dp[len(s)]


# Create an instance of the solution and test with a sample input
solution = Solution()
# Uncomment the following line to test the provided case "leetcode"
# solution.wordBreak("leetcode", ["leet", "code"])
print(solution.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
