class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.count = size  # Number of connected components
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return  # Already connected
        # Union by rank
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        self.count -= 1  # Decrement count as two components merge
class Solution:
    def findCircleNum(self,isConnected):
        n = len(isConnected)
        dsu = DSU(n)
        for i in range(n):
            for j in range(i + 1, n):  # Avoid duplicate checks by using i+1
                if isConnected[i][j]:
                    dsu.union(i, j)
        return dsu.count