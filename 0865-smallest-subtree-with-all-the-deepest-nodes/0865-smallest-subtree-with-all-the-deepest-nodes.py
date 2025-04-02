# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        # Stores the node that covers all the deepest nodes in the tree
        self.target_node = None
        # Minimum depth at which the target node is found (used for tie-breaking)
        self.min_depth = 1000
        # Maximum depth at which the deepest nodes are found
        self.max_depth = -1

    def dfs(self, node, depth):
        """
        Perform depth-first search to calculate the depth of left and right subtrees.

        Intuition:
        - Find a node whose left and right subtree depths are equal (implying it covers all deepest nodes).
        - Among such nodes, choose the one that is:
          1. At the greatest depth for the deepest nodes.
          2. If multiple nodes exist, choose the one at the shallowest depth in the tree.
        """
        if node is None:
            # Return the depth just above the null node
            return depth - 1

        # Recursively calculate the maximum depth of the left and right subtrees
        depth_l = self.dfs(node.left, depth + 1)
        depth_r = self.dfs(node.right, depth + 1)

        # Check if this node is a potential target node
        if depth_l == depth_r:
            # Condition 1: If the subtree depth is greater than the previously known max depth
            if depth_l > self.max_depth or \
            (depth_l == self.max_depth and depth < self.min_depth):
             # Condition 2: If the subtree depth matches the max depth, but this node is at a shallower depth
                self.target_node = node
                self.min_depth = depth
                self.max_depth = depth_l

        # Return the maximum depth found in the left or right subtree
        return max(depth_l, depth_r)

    def subtreeWithAllDeepest(self, root):
        self.dfs(root, 0)
        return self.target_node