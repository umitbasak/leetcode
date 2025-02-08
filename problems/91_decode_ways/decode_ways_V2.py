class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string has one way to decode
        dp[1] = 1  # one valid digit has one way

        for i in range(2, n + 1):
            # Check for valid single digit decoding.
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            # Check for valid two digit decoding.
            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

            # If no valid decodings at this position, return 0 early.
            if dp[i] == 0:
                return 0

        return dp[n]


solution = Solution()
print(solution.numDecodings("12131"))
