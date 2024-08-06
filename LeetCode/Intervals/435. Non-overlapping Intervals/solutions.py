class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda i: i[1])
        ans = 0
        k = float('-inf')

        for x, y in intervals:
            if x >= k:
                k = y
            else:
                ans += 1
        return ans
        