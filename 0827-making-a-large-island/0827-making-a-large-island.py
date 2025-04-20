class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = [i for i in range(n*n)]
        rank = [1 for i in range(n*n)]

        def find(r):
            while(r!=parent[r]):
                parent[r] = parent[parent[r]]
                r = parent[r]
            return r
        
        def union(x,y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            if rank[root_x]>= rank[root_y]:
                parent[root_y] = root_x
                rank[root_x]+=rank[root_y]
            else:
                parent[root_x] = root_y
                rank[root_y]+=rank[root_x]
        
        grid_map = dict()
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    for dx,dy in directions:
                        dr = dx+r
                        dc = dy+c
                        if 0<=dr<n and 0<=dc<n and grid[dr][dc]==1:
                            union(r*n+c,dr*n+dc)
        
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    root = find(r*n+c)
                    grid_map[root] = rank[root]
        
        max_area = max(grid_map.values(), default=0)

        for r in range(n):
            for c in range(n):
                if grid[r][c]==0:
                    visited = set()
                    area = 1
                    for dx,dy in directions:
                        dr = dx+r
                        dc = dy+c
                        if 0<=dr<n and 0<=dc<n and grid[dr][dc]==1:
                            root = find(dr*n+dc)
                            if root not in visited:
                                visited.add(root)
                                area+=rank[root]
                    max_area = max(max_area,area)
        if max_area > 0:
            return max_area
        else:
            return n*n

