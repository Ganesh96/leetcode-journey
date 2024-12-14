class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaves) -> list:
            if root is None:
                return leaves

            left = dfs(root.left, leaves)
            right = dfs(root.right, leaves)

            if root.left is None and root.right is None:  # Check if it's a leaf node
                leaves.append(root.val)
            return leaves

        leaves1 = list()
        leaves2 = list()
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        print(leaves1, leaves2)  # Debugging output
        return leaves1 == leaves2