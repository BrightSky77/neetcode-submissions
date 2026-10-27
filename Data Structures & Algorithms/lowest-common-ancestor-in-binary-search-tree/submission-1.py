# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        min_candidate = min(p.val,q.val)
        max_candidate = max(p.val,q.val)
        ans = 0
        while True:
            if min_candidate<=root.val<=max_candidate:
                ans = root
                break
            elif (min_candidate < root.val) and (max_candidate<root.val):
                root = root.left
            
            elif (min_candidate > root.val) and (max_candidate>root.val):
                root = root.right

        return ans   