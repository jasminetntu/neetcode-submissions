# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        # INORDER -> ALWAYS ASCENDING IF VALID
        # inorder = []

        # def valid(node):
        #     if node is None:
        #         return
            
        #     valid(node.left)
        #     inorder.append(node.val)
        #     valid(node.right)

        # valid(root)

        # for i in range(len(inorder) - 1):
        #     if inorder[i] >= inorder[i + 1]:
        #         return False
        # return True
            
        
        # WITHOUT INORDER
        # if go left -> we know the node must be less than all nodes before it -> 
        # update max to reflect new highest the node can be

        # if go right -> we know node must be greater than all noddes before it ->
        # update min to reflect new lowest node can be

        def valid(node, minSoFar, maxSoFar):
            if node is None:
                return True

            if node.val <= minSoFar or node.val >= maxSoFar:
                return False

            # minSoFar, maxSoFar = min(minSoFar, node.val), max(maxSoFar, node.val)

            return valid(node.left, minSoFar, node.val) and valid(node.right, node.val, maxSoFar)
        
        
        return valid(root, float('-inf'), float('inf'))