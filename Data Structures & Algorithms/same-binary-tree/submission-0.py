# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False 
            left_sub_tree = dfs(p.left,q.left)
            right_sub_tree = dfs(p.right,q.right)
            return (left_sub_tree and right_sub_tree)
        
        return dfs(p,q)
            

        