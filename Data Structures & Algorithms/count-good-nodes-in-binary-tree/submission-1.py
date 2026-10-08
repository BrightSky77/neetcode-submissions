# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        output = 0
        maxVal = -float("inf")
        def dfs(root,maxVal):
            nonlocal output
            if not root:
                return
            if root.val >= maxVal:
                output += 1
            maxVal = max(root.val,maxVal)
            dfs(root.left,maxVal)
            dfs(root.right,maxVal)
        dfs(root,maxVal)
        return output



            
            


        