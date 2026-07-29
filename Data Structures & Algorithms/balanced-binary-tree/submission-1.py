# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height-balanced = max diff in depth of 2 subtrees is 1

        if root is None:
            return True

        isBalanced = True

        def compareDepth(node):
            nonlocal isBalanced

            if node is None:
                return 0
            
            leftDepth = compareDepth(node.left)
            rightDepth = compareDepth(node.right)

            if abs(leftDepth - rightDepth) > 1:
                isBalanced = False
            
            return 1 + max(leftDepth, rightDepth)
        
        compareDepth(root)

        return isBalanced
        