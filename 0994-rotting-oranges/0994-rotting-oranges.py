class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        time = fresh = 0
        q = deque()
 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c,0))
        direction = [(-1,0),(1,0),(0,1),(0,-1)]

        while q:
            r,c, minutes = q.popleft()
            time = max(time, minutes)
            for dr, dc in direction:
                nr,nc = r+ dr, c+dc
                if 0<=nr<rows and 0<= nc < cols and grid[nr][nc]==1:
                    fresh-=1
                    grid[nr][nc] =2
                    q.append((nr,nc,minutes+1))
        return time if fresh==0 else -1

        