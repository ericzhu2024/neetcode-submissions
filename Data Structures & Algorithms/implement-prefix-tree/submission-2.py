class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                new = TrieNode()
                cur.children[c] = new
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end
        
    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True