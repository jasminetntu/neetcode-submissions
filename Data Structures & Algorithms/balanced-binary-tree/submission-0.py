# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height-balanced = max diff in depth of 2 subtrees is 1
        self.isBalanced = True

        if root is None:
            return True
        
        def compareDepth(node):
            if node is None:
                return 0
            
            leftDepth = compareDepth(node.left)
            rightDepth = compareDepth(node.right)

            if abs(leftDepth - rightDepth) > 1:
                self.isBalanced = False
            
            return 1 + max(leftDepth, rightDepth)
        
        compareDepth(root)

        return self.isBalanced
        