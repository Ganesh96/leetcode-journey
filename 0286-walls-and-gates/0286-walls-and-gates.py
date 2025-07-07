from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        q = deque([])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c]==0:
                    q.append((r,c,0))
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]] 
        while(q):
            x,y,d = q.popleft()

            for dr,dc in directions:
                nr = x+dr
                nc = y+dc
                if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc]==2147483647:
                    q.append((nr,nc,d+1))
                    rooms[nr][nc] = d+1
        return rooms
