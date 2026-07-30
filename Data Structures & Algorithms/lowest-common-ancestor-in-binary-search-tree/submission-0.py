# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # --- SOL FOR BST ---
        def findLCA(node): # does not need helper function
            if node is None:
                return
            
            if max(p.val, q.val) < node.val:
                return findLCA(node.left)
            elif min(p.val, q.val) > node.val:
                return findLCA(node.right)
            
            return node
        
        return findLCA(root)

        # --- SOL FOR NON BST ---
        # lca = root

        # def hasNode(node, target): # bool
        #     if node is None:
        #         return False
            
        #     if node == target:
        #         return True
            
        #     return hasNode(node.left, target) or hasNode(node.right, target)

        # def findLCA(node):
        #     nonlocal lca

        #     if node is None:
        #         return
            
        #     leftHasP = hasNode(node.left, p)
        #     leftHasQ = hasNode(node.left, q)
        #     rightHasP = hasNode(node.right, p)
        #     rightHasQ = hasNode(node.right, q)

        #     # print(leftHasP, leftHasQ, rightHasP, rightHasQ, lca.val)

        #     if (leftHasP and rightHasQ) or (leftHasQ and rightHasP) or (node == q or node == p):
        #         lca = node

        #     if leftHasP and leftHasQ:
        #         findLCA(node.left)
        #     elif rightHasP and rightHasQ:
        #         findLCA(node.right)

        #     return
            
        # findLCA(root)
        # return lca



        