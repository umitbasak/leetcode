class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        r = len(s1)

        originalStringDict = {}
        for c in s1:
            if c not in originalStringDict:
                originalStringDict[c] = 0
            originalStringDict[c] += 1

        s2Dict = {}
        for i in range(r):
            if s2[i] not in s2Dict:
                s2Dict[s2[i]] = 0
            s2Dict[s2[i]] += 1

        if s2Dict == originalStringDict:
            return True

        while r < len(s2):

            if s2Dict[s2[r - len(s1)]] > 1:
                s2Dict[s2[r - len(s1)]] -= 1
            else:
                s2Dict.pop(s2[r - len(s1)])

            if s2[r] not in s2Dict:
                s2Dict[s2[r]] = 0
            s2Dict[s2[r]] += 1

            print(f"r:{r} originalStringDict:{originalStringDict}, s2Dict:{s2Dict}")
            if s2Dict == originalStringDict:
                return True

            r += 1

        return False


solution = Solution()
# print(solution.checkInclusion("ab", "eidbaooo"))
print(solution.checkInclusion("adc", "dcda"))
