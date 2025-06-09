# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results=[]
        def bfs(root):
            if not root:
                return []
            queue = deque([root])
            
            while queue:
                level_size = len(queue)
                level_nodes=[]
                for i in range(0, level_size):
                    node=queue.popleft()
                    level_nodes.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    
                results.append(level_nodes)

        bfs(root)
        return results
        