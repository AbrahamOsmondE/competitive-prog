# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [float('-inf')]

        def postorder(node):
            if node:
                left = postorder(node.left)
                right = postorder(node.right)
                res = max(node.val, node.val + left, node.val + right)
                ans[0] = max(ans[0], res, node.val + left + right)
                return res
            return 0
        postorder(root)

        return ans[0]
        