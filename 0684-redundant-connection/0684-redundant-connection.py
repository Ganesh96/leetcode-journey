class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N+1)]
        rank = [1] * (N+1)

        def find(n):
            root = par[n]
            while root!=par[root]:
                par[root] = par[par[root]]
                root = par[root]
            return root
        
        def union(n1,n2):
            root1 = find(n1)
            root2 = find(n2)
            if root1==root2:
                return False
            
            if rank[root1] > rank[root2]:
                par[root2] = root1
                rank[root1]+=rank[root2]
            
            else:
                par[root1] = root2
                rank[root2]+=rank[root1]
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
