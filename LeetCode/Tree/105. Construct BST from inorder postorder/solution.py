# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Use preorder to determine roots
        # Use inorder to determine children
        preOrderIndex = [0]
        def arrayToTree(left,right):
            if left > right:
                return None
            
            print(preOrderIndex)
            preOrderValue = preorder[preOrderIndex[0]]
            tree = TreeNode(preOrderValue)

            preOrderIndex[0] += 1
            tree.left = arrayToTree(left, inOrderIndex[preOrderValue] - 1)
            tree.right = arrayToTree(inOrderIndex[preOrderValue] + 1, right)
            return tree
        
        inOrderIndex = {}
        for index, value in enumerate(inorder):
            inOrderIndex[value] = index
        
        return arrayToTree(0, len(inorder) - 1)
        