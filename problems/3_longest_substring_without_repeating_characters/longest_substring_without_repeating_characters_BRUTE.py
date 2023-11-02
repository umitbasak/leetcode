class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encountered = set()
        maxLength = 0
        currentLength = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in encountered:
                    currentLength = 0
                    encountered = set()
                    break
                encountered.add(s[j])
                currentLength += 1
                maxLength = max(currentLength, maxLength)

        return maxLength


solution = Solution()
# print(solution.lengthOfLongestSubstring("abcabcbb"))
# print(solution.lengthOfLongestSubstring("bbbbb"))
# print(solution.lengthOfLongestSubstring("pwwkew"))
# print(solution.lengthOfLongestSubstring("dvdf"))
print(solution.lengthOfLongestSubstring("jbpnbwwd"))
