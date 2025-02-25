class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        edge_list = []
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    edge_list.append((i, j))
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n1):
            res = n1
            while res!= par[res]:
                par[res]=par[par[res]]
                res = par[res]
            return res
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return 0
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] +=rank[p1]
            else:
                par[p2] = p1
                rank[p1]+=rank[p2]
            return 1
        
        provinces = n
        for n1,n2 in edge_list:
            provinces-=union(n1,n2)
        return provinces