class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, node, "", ans)
        return ans
    
    
    def dfs(self, board, i, j, node, path, ans):
        if node.isWord:
            ans.append(path)
            node.isWord = False
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return
        
        val = board[i][j]
        board[i][j] = "#"
        for pair in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            self.dfs(board, i+pair[0], j+pair[1], node.children[val], path+val, ans)
        board[i][j] = val
