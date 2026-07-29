# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
                return False
            
            leftSame = compare(node1.left, node2.left)
            rightSame = compare(node1.right, node2.right)
            
            # print(node1.val, node2.val, leftSame, rightSame)

            return leftSame and rightSame and node1.val == node2.val
        
        def findSubtree(node1, node2):
            if node1 is None:
                return False

            if node1.val == node2.val:
                if compare(node1, node2):
                    return True
            
            leftSubtree = findSubtree(node1.left, node2)
            rightSubtree = findSubtree(node1.right, node2)

            return leftSubtree or rightSubtree
        
        return findSubtree(root, subRoot)