class TreeNode:
    def __init__(self):
        self.child = dict()
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TreeNode()
            node = node.child[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        def dfs(i, node):
            if i == len(word):
                return node.is_end
            ch = word[i]

            if ch == '.':
                for value in node.child.values():
                    if dfs(i+1,value):
                        return True
                return False
            else: 
                if ch not in node.child:
                    return False
                return dfs(i+1, node.child[ch])
                

        return dfs(0, node)