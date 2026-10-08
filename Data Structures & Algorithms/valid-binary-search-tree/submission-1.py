# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def valid_dfs(node,left,right):
            if not node:
                return True
            if not (left<node.val<right):
                return False
            return (valid_dfs(node.left,left,node.val) and valid_dfs(node.right,node.val,right))
            
        return valid_dfs(root, float("-inf"), float("inf"))

        