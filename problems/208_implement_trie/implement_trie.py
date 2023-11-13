class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for i in range(len(word)):
            if word[i] not in current.children:
                current.children[word[i]] = TrieNode()
            current = current.children[word[i]]

        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for i in range(len(word)):
            if word[i] not in current.children:
                return False
            current = current.children[word[i]]
        if not current.isEndOfWord:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
print(obj.search("word"))
print(obj.search("wor"))
# param_3 = obj.startsWith(prefix)
