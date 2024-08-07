class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        i = 0
        ans = [0,0,0]

        for x,y,z in triplets:
            if ans == target:
                return True
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            ans = [
                max(ans[0], x),
                max(ans[1], y),
                max(ans[2], z)
            ]

        return ans == target