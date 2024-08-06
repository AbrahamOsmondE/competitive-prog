class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i: i[0])
        ans = []
        for i in range(len(intervals)):
            curr = intervals[i]
            if len(ans) == 0:
                ans.append(curr)
                continue

            if ans[-1][1] >= curr[0]:
                ans[-1][1] = max(curr[1], ans[-1][1])
            else:
                ans.append(curr)

        return ans
        