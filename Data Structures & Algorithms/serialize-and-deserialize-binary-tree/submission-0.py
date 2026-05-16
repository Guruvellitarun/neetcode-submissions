# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # i am trying with Breath frist search
        q = collections.deque()
        q.append(root)
        data = []
        while q:
            node = q.popleft()
            if node:
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                data.append('NA')
            
        return ",".join(data)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        
        if data[0] == "NA":
            return None
    
        root = TreeNode(int(data[0]))
        q = collections.deque()
        q.append(root)

        i = 1
        while q and i < len(data):
            node = q.popleft()
            # left child
            if data[i] != 'NA':
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i += 1

            # right child
            if i < len(data) and data[i] != "NA":
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
            i += 1
        return root   

                        
