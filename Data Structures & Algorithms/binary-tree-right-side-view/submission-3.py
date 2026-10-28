# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        def bfs(node):
            queue = deque([node])
                
            while queue:
                lenQ = len(queue)
                sub_tree = []
                for i in range(lenQ):
                    q = queue.popleft()
                    sub_tree.append(q.val)
                    if q.left:
                        queue.append(q.left)
                    if q.right:
                        queue.append(q.right)

                res.append(sub_tree.pop())
        bfs(root)
        return res

                


