class TreeNode:
    def __init__(self):
        self.child = dict()
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TreeNode()
            node = node.child[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.child:
                return False
            node = node.child[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.child:
                return False
            node = node.child[ch]
        return True
        
        