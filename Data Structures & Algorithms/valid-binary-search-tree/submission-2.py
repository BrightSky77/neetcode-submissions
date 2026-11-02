# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validDFS(node,left,right):
            if not node:
                return True
            if not (left<node.val<right):
                return False
            return (validDFS(node.left,left,node.val)) and (validDFS(node.right,node.val,right)) 





        return validDFS(root,float("-inf"),float("inf"))

        