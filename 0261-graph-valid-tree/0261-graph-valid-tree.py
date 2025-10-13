class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        visit = set()

        def find(u):
            while parent[u]!=u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        for a,b in edges:
            U = find(a)
            V = find(b)
            if U==V:
                return False
            parent[V] = U
        
        for i in range(n):
            visit.add(find(i))
        return len(visit)==1