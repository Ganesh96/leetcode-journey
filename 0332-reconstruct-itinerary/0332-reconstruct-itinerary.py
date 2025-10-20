class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:


        graph = defaultdict(list)
        itinerary = []
        START = 'JFK'

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)
        
        for src,dst in sorted(tickets,reverse=True):
            graph[src].append(dst)

        dfs(START)

        return itinerary[::-1]