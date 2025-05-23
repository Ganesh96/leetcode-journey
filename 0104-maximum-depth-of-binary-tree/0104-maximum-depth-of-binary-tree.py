# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def height(node):
            if node is None:
                return 0
            
            left = height(node.left)
            right = height(node.right)

            return max(left, right) + 1
        h = height(root)

        return h
        