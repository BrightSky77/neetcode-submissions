# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        def bfs(node):
            queue = deque([node])
            while queue:
                sub_list = []
                for i in range(len(queue)):
                    n = queue.popleft()
                    sub_list.append(n.val)
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                if sub_list:
                    ans.append(sub_list)
        bfs(root)
        return ans 

        


                
