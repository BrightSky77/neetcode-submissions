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
        cur = root
        answer = []
        def bfs(cur):
            q = deque([cur])
            while q:
                q_length = len(q)
                level = []

                for _ in range(q_length):
                    cur_tree = q.popleft()
                    level.append(cur_tree.val)
                    if cur_tree.left:
                        q.append(cur_tree.left)
                    if cur_tree.right:
                        q.append(cur_tree.right)
                answer.append(level)
        bfs(cur)
        return answer

                
