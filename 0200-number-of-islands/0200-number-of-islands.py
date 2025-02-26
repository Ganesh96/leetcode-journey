class UnionFind:
    def __init__(self, grid):
        self.parent = {}
        self.rank = {}
        self.count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.parent[(i, j)] = (i, j)
                    self.rank[(i, j)] = 1
                    self.count += 1
        print(self.parent)
        print(self.rank)
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:

            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
class Solution:
    def numIslands(self,grid):
        if not grid:
            return 0
        
        uf = UnionFind(grid)
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                            uf.union((i, j), (x, y))
        print(uf.parent)
        print(uf.rank)
        return uf.count