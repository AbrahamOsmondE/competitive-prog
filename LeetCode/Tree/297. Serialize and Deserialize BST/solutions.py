# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(node):
            if node:
                res.append(str(node.val) + ",")
                preorder(node.left)
                preorder(node.right)
            else:
                res.append("None,")
        preorder(root)
        return "".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = collections.deque(data.split(','))
        def preorder():
            if arr[0] == 'None':
                arr.popleft()
                return None
            root = TreeNode(arr[0])
            arr.popleft()
            root.left = preorder()
            root.right = preorder()
            return root
            
            
        return preorder()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))