# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True

            left_h = height(root.left)
            right_h = height(root.right)

            if abs(left_h - right_h) > 1:
                return False
            
            return dfs(root.left) and dfs(root.right)
        
        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right))+1

        if not root:
            return True

        return dfs(root)