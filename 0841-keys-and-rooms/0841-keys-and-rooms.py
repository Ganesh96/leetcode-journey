class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()

        def dfs(R):
            visit.add(R)
            for room in rooms[R]:
                if room not in visit:
                    dfs(room)

        dfs(0)
        return len(visit)==len(rooms)