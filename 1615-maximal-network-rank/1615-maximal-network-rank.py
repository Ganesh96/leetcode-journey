class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        res = 0

        for city1,city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
        
        for city1,city2 in itertools.combinations(graph.keys(),2):
            connected = 1 if city2 in graph[city1] else 0
            city1_connect = len(graph[city1])
            city2_connect = len(graph[city2])

            res = max(city1_connect + city2_connect -connected,res)
        return res