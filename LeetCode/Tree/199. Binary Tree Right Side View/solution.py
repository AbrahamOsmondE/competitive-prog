# Just take from 102 and modify the return value

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = collections.deque([[root, 0]])
        temp = []
        while len(queue):
            node, depth = queue.popleft()
            if node:
                temp.append([node.val, depth])
                queue.append([node.left, depth + 1])
                queue.append([node.right, depth + 1])
        depth = max([i[1] for i in temp])
        ans = [[] for _ in range(depth + 1)]

        for val, depth in temp:
            ans[depth].append(val)
        return [i[-1] for i in ans]