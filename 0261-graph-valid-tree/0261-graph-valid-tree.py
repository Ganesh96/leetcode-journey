class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges)!=n-1):
            return False
        adj_list = dict()
        visit = set()

        for a,b in edges:
            if a in adj_list:
                adj_list[a].append(b)
            else:
                adj_list[a] = [b]
            if b in adj_list:
                adj_list[b].append(a)
            else:
                adj_list[b] = [a]

        def dfs(N,status):
            if N in visit:
                return False
            visit.add(N)
            for neighbor in adj_list[N]:
                print(visit)
                status = status and dfs(neighbor,status)
            return True
        
        return dfs(0,True)