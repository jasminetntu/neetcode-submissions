# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def compare(isSame, pNode, qNode):
            if pNode is None and qNode is None:
                return True
            elif (pNode is None and qNode is not None) or (pNode is not None and qNode is None):
                return False
            
            leftSame = compare(isSame, pNode.left, qNode.left)
            rightSame = compare(isSame, pNode.right, qNode.right)

            return leftSame and rightSame and (pNode.val == qNode.val)

        
        return compare(True, p, q)