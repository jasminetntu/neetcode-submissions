# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def calc_depth(node):
            if node is None:
                return 0
            
            left_depth = 1 + calc_depth(node.left)
            right_depth = 1 + calc_depth(node.right)

            return max(left_depth, right_depth)

        return calc_depth(root)
        