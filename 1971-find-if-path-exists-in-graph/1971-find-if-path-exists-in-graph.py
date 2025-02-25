class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            root = x
            while parent[root]!=root:
                parent[root] = parent[parent[root]]
                root = parent[root]
            return root

        def union(x,y):
            x_root = find(x)
            y_root = find(y)

            if x_root == y_root:
                return 0
            
            if rank[x_root]>rank[y_root]:
                parent[y_root] = x_root
                rank[x_root]+=rank[y_root]

            else:
                parent[x_root] = y_root
                rank[y_root]+=rank[x_root]
            return 1
        
        for s,d in edges:
            if s<d:
                union(s,d)
            else:
                union(d,s)
        return True if parent[source]==parent[destination] else False