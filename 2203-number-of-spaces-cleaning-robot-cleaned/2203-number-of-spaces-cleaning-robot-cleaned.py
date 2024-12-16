class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        
        M = len(room)
        N = len(room[0])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirIdx = 0

        cleaned = 0
        i, j = 0, 0
        while True:
            if room[i][j] == 0: 
                cleaned += 1

            ni, nj, curDir = i + dirs[dirIdx][0], j + dirs[dirIdx][1], dirIdx
            while not (0 <= ni < M) or not (0 <= nj < N) or (room[ni][nj] == 1):
                dirIdx = (dirIdx + 1) % 4
                ni, nj = i + dirs[dirIdx][0], j + dirs[dirIdx][1]
                if dirIdx == curDir:
                    return cleaned

            if room[i][j] == dirIdx + 4:
                return cleaned

            room[i][j] = dirIdx + 4

            i, j = ni, nj
            
                