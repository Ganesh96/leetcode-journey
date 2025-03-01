class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        normal_color = image[sr][sc]

        def dfs(r,c):
            if not(0 <= r < rows and 0 <= c < cols):
                return
            if visited[r][c] == True or image[r][c]!=normal_color:
                return 

            visited[r][c] = True
            image[r][c] = color

            dfs(r-1,c) # up
            dfs(r+1,c) # down
            dfs(r,c-1) # left
            dfs(r,c+1) # right
        
        dfs(sr,sc)
        return image