from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize a DP array where dp[i] represents whether s[i:] can be segmented into words from wordDict.
        dp = [False] * (len(s) + 1)
        # The empty substring is always "segmentable"
        dp[len(s)] = True

        # Process the string from the end towards the beginning
        for i in range(len(s) - 1, -1, -1):
            # Try each word in the dictionary
            for w in wordDict:
                # Check if the remaining substring from i is long enough to match the word w
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    # Set dp[i] to true if the substring starting after w can be segmented
                    dp[i] = dp[i + len(w)]
                # If we already found a valid segmentation at i, exit the loop early
                if dp[i]:
                    break

        # Finally, return whether the whole string s can be segmented into dictionary words
        return dp[0]


# Create an instance of the solution and test with a sample input
solution = Solution()
# Uncomment the following line to test the provided case "leetcode"
# solution.wordBreak("leetcode", ["leet", "code"])
solution.wordBreak("aaaaaaa", ["aaaa", "aaa"])
