# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        arr = [None]
        def post(node, p, q):
            count = 0
            if node:
                count += post(node.left, p, q)
                count += post(node.right, p, q)

                if node == p or node == q:
                    count += 1

                if count == 2 and not arr[0]:
                    arr[0] = node
                    return count

            return count
                
        post(root, p, q)
        return arr[0]