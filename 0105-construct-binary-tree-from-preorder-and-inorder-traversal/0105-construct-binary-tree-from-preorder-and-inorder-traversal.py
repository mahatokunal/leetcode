# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {value: idx for idx, value in enumerate(inorder)}

        def build(L, R, idx_pre):
            if L>R:
                return None, idx_pre
            root_val=preorder[idx_pre]
            idx_pre+=1
            mid=pos[root_val]

            node=TreeNode(root_val)
            node.left, idx_pre = build(L, mid-1, idx_pre)
            node.right, idx_pre = build(mid+1, R, idx_pre)

            return node, idx_pre
        
        root, _ = build(0, len(inorder)-1, 0)
        return root