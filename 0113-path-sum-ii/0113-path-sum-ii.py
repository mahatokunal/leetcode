# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results=[]
        def dfs(node, path, sum):
            if not node:
                return
            
            path.append(node.val)
            sum+=node.val

            if not node.left and not node.right:
                if sum==targetSum:
                    results.append(list(path))
            else:
                dfs(node.left, path, sum)
                dfs(node.right, path, sum)

            path.pop()
        
        dfs(root, [], 0)
        return results
        