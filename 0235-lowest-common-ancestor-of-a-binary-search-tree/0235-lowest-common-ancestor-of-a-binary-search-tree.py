# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<q.val:
            small = p.val
            large = q.val
        else:
            small = q.val
            large = p.val
        node = root
        while node:
            if (small<node.val and node.val<large) or (small==node.val) or (large==node.val):
                return node
            if small<node.val and large<node.val:
                node=node.left
            if small>node.val and large>node.val:
                node=node.right
        