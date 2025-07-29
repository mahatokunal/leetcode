# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        def depth(node):
            if node==None:
                return 0
            lHeight = depth(node.left)
            rHeight = depth(node.right)
            if lHeight is False or rHeight is False or lHeight-rHeight>1 or lHeight-rHeight<-1:
                print(node.val, lHeight, rHeight, lHeight-rHeight)
                return False
            return 1 + max(lHeight, rHeight) 
        return depth(root)!=False