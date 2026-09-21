# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # preorder: node first -> dont know left/right
        # ^ root is always the first

        # inorder: go left first -> dont know from where
        # ^ we know that everything to the left of root is the left subtree
        # ^ and everything to the right of root is right subtree

        # recursive
        # preorder -> queue (iterate left -> right)
        # find curr node -> left of it = left subtree, right of it = right subtree

        # keep track of curr i & prev i 
        # left must be < curr i 
        
        # node.left = recurse(0)

        

        # return curr node

        indices = {}
        for i in range(len(inorder)):
            indices[inorder[i]] = i
        
        def makeTree(start, end):
            if end - start == 0: # nothing in range
                return None
            # if len(preorder) == 0:
            #     return None
            
            value = preorder.pop(0)
            node = TreeNode(value)

            # find idx of value
            idx = indices[value]

            node.left = makeTree(start, idx)
            node.right = makeTree(idx + 1, end)

            return node
        
        return makeTree(0, len(preorder))
        