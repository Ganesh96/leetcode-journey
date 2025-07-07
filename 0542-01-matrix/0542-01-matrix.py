class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        
        dist = list()
        R,C = len(mat), len(mat[0])

        for r in range(R):
            row = list()
            for c in range(C):
                if mat[r][c] == 0:
                    row.append(0)
                else:
                    row.append(float('inf'))
            dist.append(row)
        
        q = deque()
        for r in range(R):
            for c in range(C):
                if mat[r][c]==0:
                    q.append((r,c))
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        while q:
            x,y = q.popleft()
            for dr,dc in directions:
                nr = x + dr
                nc = y + dc
                if (0<= nr<R and 0<=nc<C) and (dist[nr][nc]>dist[x][y]+1):
                    dist[nr][nc] =dist[x][y]+1
                    q.append((nr,nc))
        return dist  
