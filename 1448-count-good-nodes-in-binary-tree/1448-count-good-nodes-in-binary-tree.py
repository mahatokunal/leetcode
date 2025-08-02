# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        return self.dfs(root, -10001, count)
    
    def dfs(self, node, lastGreatest, count):
        if not node:
            return count
        if node.val>=lastGreatest:
            lastGreatest=node.val
            count+=1
        count = self.dfs(node.left, lastGreatest, count)
        count = self.dfs(node.right, lastGreatest, count)
        return count
        