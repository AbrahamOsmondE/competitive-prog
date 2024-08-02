# Solution is based on the fact that an in order traversal of a sorted BST will return a sorted array

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = []
        def in_order(node):
            if node:
                in_order(node.left)
                ans.append(node.val)
                in_order(node.right)
        in_order(root)
        for i in range(len(ans) - 1):
            if ans[i] >= ans[i+1]:
                return False
        return True