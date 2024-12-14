# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root,leaves) -> list:
            if root == None:
                return
            if not root.left and not root.right:  # Check if it's a leaf node
                leaves.append(root.val)

            dfs(root.left,leaves)
            dfs(root.right,leaves)
            return leaves

        leaves1 = list()
        leaves2 = list()
        l1 = dfs(root1,leaves1)
        l2 = dfs(root2,leaves2)
        print(l1,"#",l2)
        return l1==l2
        