class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        xleft = 0
        xright = len(intervals) - 1
        x = newInterval[0]
        while xleft <= xright:
            xmid = (xleft + xright) // 2
            curr = intervals[xmid]
            if curr[0] <= x and curr[1] >= x:
                break
            elif curr[0] > x:
                xright = xmid - 1
            else:
                xleft = xmid + 1
        
        yleft = 0
        yright = len(intervals) - 1
        y = newInterval[1]

        while yleft <= yright:
            ymid = (yleft + yright) // 2
            curr = intervals[ymid]
            if curr[0] <= y and curr[1] >= y:
                break
            elif curr[1] < y:
                yleft = ymid + 1
            else:
                yright = ymid - 1
        
        ans = []
        xmin = min(intervals[xmid][0], newInterval[0]) if intervals[xmid][1] >= newInterval[0] else newInterval[0]

        end = xmid if intervals[xmid][1] >= newInterval[0] else xmid + 1
        for i in range(end):
            ans.append(intervals[i])
        
        ymax = max(intervals[ymid][1], newInterval[1]) if intervals[ymid][0] <= newInterval[1] else newInterval[1]

        ans.append([xmin, ymax])

        start = ymid + 1
        if intervals[ymid][0] > newInterval[1]:
            start = ymid
        
        for i in range(start, len(intervals)):
            ans.append(intervals[i])
        
        return ans