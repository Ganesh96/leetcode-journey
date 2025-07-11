class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addNode(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()

        for w in words:
            root.addNode(w)
        
        rows, cols = len(board),len(board[0])
        res, visited = set(), set()

        def dfs(r,c,node,word):
            if not (0<=r<rows and 0<=c<cols):
                return
            if board[r][c] not in node.children:
                return
            if (r,c) in visited:
                return
            
            visited.add((r,c))

            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r,c+1,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r-1,c,node,word)
            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)