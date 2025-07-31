# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pVal=p.val
        qVal=q.val
        node = root
        while node:
            nodeVal = node.val
            if pVal<nodeVal and qVal<nodeVal:
                node = node.left
            elif pVal>nodeVal and qVal>nodeVal:
                node = node.right
            else:
                return node 