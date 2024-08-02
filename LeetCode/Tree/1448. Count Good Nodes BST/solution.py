# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        def pre_order(node, curr):
            if not node:
                return
            if node.val >= curr:
                ans[0] += 1
            pre_order(node.left, max(node.val, curr))
            pre_order(node.right, max(node.val, curr))
        pre_order(root, float('-inf'))
        return ans[0]     