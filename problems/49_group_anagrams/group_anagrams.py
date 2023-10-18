from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        # for every string in strs create an array representing all characters
        # in the alphabet and show how many characters do the string have
        # inside the array
        for s in strs:
            count = [0] * 26  # for representing every character the alphabet

            # populate the count array, for example if the string is aaa the
            # count array will be like = [3, 0, 0 ...]
            for c in s:
                count[ord(c) - ord("a")] += 1

            # transform the count array into a tuple for python language
            # purposes, then put the count array inside the "res" dictionary
            # that corresponds to the same array, this way the anagrams will
            # be on the same key
            res[tuple(count)].append(s)
        return list(res.values())
