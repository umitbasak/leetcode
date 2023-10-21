class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        result = ""

        for str in strs:
            str = ":" + str + ";"
            result += str

        print(result)
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        result = []
        word = ""
        previousChar = ""

        for char in str:
            if char == ":" and previousChar != ":":
                previousChar = char
                word = ""
                continue
            if char == ";" and len(word) > 0:
                previousChar = char
                result.append(word)
                continue
            word += char
            previousChar = char

        print(result)
        return result


solution = Solution()

# encodedString1 = solution.encode(["apple", "banana", "fig", "tangerine"])
# solution.decode(encodedString1)

encodedString2 = solution.encode(["we", "say", ":", "yes"])
solution.decode(encodedString2)
