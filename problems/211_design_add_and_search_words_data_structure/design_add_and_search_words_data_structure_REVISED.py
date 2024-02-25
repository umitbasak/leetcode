class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWordEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                cur.children[char] = TrieNode()
                cur = cur.children[char]
        cur.isWordEnd = True

    def search(self, word: str) -> bool:
        def dfs(trie, i):
            current = trie
            if i == len(word):
                return current.endOfWord

            char = word[i]
            if char != ".":
                if char not in current.children:
                    return False
                return dfs(current.children[char], i + 1)
            else:
                for child in current.children:
                    if dfs(current.children[child], i + 1):
                        return True
                return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
