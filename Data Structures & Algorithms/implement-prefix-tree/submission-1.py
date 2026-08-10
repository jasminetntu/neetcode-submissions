class TrieNode:
    def __init__(self, value=0, isEnd=False):
        self.value = value
        self.isEnd = isEnd
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # print('insert')
        node = self.root
        for c in word:
            if node.children[ord(c) - ord('a')] is None:
                node.children[ord(c) - ord('a')] = TrieNode()
            node.children[ord(c) - ord('a')].value += 1
            node = node.children[ord(c) - ord('a')]
        node.isEnd = True

    def search(self, word: str) -> bool:
        # print('search')
        node = self.root
        for c in word:
            if node.children[ord(c) - ord('a')] is None:
                return False
            node = node.children[ord(c) - ord('a')]
        
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        # print('startsWith')
        node = self.root
        for c in prefix:
            if node.children[ord(c) - ord('a')] is None:
                return False
            node = node.children[ord(c) - ord('a')]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)