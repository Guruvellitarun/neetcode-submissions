# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        p_queue = deque()
        p_queue.append(p)
        q_queue = deque()
        q_queue.append(q)
        while p_queue and q_queue:
            p_val = p_queue.popleft()
            q_val = q_queue.popleft()
            if p_val.val != q_val.val or (q_val.left and not p_val.left) or (q_val.right and not p_val.right) or (p_val.right and not q_val.right) or (p_val.left and not q_val.left):
                return False
            if p_val.left and q_val.left:
                p_queue.append(p_val.left)
                q_queue.append(q_val.left)
            if p_val.right and q_val.right:
                p_queue.append(p_val.right)
                q_queue.append(q_val.right)
        return True