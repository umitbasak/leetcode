class Solution:
    def countSubstrings(self, s: str) -> int:
        if s is None or len(s) < 1:
            return 0
        totalNumberOfPalindroms = 0

        for i in range(len(s)):
            totalNumberOfPalindroms += self.expandFromMiddle(
                s, i, i
            ) + self.expandFromMiddle(s, i, i + 1)

        return totalNumberOfPalindroms

    # expands from the given indexes and returns the number of palindroms that
    # are centered around these indexes
    def expandFromMiddle(self, s, i, j):
        if s is None or i > j:
            return 0
        numberOfPalindromsCentered = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            numberOfPalindromsCentered += 1
            i -= 1
            j += 1

        return numberOfPalindromsCentered
