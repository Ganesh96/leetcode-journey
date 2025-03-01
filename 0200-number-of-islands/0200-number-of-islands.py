class Solution:
    def numIslands(self,grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        par = {}
        rank = {}
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    par[(i, j)] = (i, j)
                    rank[(i, j)] = 1
                    count += 1

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                            if union((i, j), (x, y)):
                                count -= 1

        return count