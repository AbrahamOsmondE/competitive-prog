class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = []
        curr = 0
        for i in height:
            left.append(max(curr, i))
            curr = max(curr, i)
        
        right = []
        curr = 0
        for i in reversed(height):
            right.append(max(curr, i))
            curr = max(curr, i)
        right.reverse()
        ans = 0
        for i in range(1, len(height)-1):
            water = min(left[i-1], right[i+1]) - height[i]
            if water > 0:
                ans += water
        return ans