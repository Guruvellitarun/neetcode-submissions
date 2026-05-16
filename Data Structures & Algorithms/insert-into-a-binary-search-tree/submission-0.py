# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        
        temp = root
        while True:
            if temp.val > val:
                if temp.left is None:
                    temp.left = TreeNode(val)
                    return root
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = TreeNode(val)
                    return root
                temp = temp.right