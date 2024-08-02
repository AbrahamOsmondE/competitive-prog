# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = []
        def in_order(node):
            if node:
                in_order(node.left)
                ans.append(node.val)
                in_order(node.right)
        in_order(root)
        return ans[k-1]