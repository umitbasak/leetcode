class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.discard(s[left])
                left += 1
            charSet.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen


solution = Solution()
# print(solution.lengthOfLongestSubstring("abcabcbb"))
# print(solution.lengthOfLongestSubstring("bbbbb"))
# print(solution.lengthOfLongestSubstring("pwwkew"))
# print(solution.lengthOfLongestSubstring("dvdf"))
print(solution.lengthOfLongestSubstring("abba"))
