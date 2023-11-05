class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        maxContinuous = 0

        left = 0
        right = 0

        while right < len(s):
            if s[right] in charCount:
                charCount[s[right]] += 1
            else:
                charCount[s[right]] = 1
            windowLength = right - left + 1
            if windowLength - max(charCount.values()) <= k:
                maxContinuous = max(maxContinuous, windowLength)
                right += 1
            else:
                while windowLength - max(charCount.values()) > k:
                    charCount[s[left]] -= 1
                    left += 1
                    windowLength = right - left + 1
                else:
                    right += 1

        return maxContinuous


solution = Solution()
print(solution.characterReplacement("AABABBA", 1))
