# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0

        def depth(node):
            if node==None:
                return 0
            lHeight = depth(node.left)
            rHeight = depth(node.right)
            diameter = lHeight + rHeight
            if diameter > self.maxD:
                self.maxD = diameter
            return 1 + max(lHeight, rHeight)
        
        depth(root)

        return self.maxD