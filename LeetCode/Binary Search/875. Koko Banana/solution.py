class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        right = max(piles)
        left = 1
        while left < right:
            mid = (left + right) // 2
            time = sum([math.ceil(float(i) / mid) for i in piles])
            if time <= h:
                right = mid
            else:
                left = mid + 1
                
        return right