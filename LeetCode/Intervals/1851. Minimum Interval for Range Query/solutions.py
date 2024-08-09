class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort(key=lambda i: (i[0], i[1]))
        pq = []
        res = {}
        curr = 0

        for num in sorted(queries):
            while pq and pq[0][2] < num:
                heapq.heappop(pq)

            while curr < len(intervals):
                if intervals[curr][0] > num:
                    break
                if intervals[curr][1] < num:
                    curr += 1
                    continue
                x,y = intervals[curr]
                currInt = (y - x + 1, x, y)
                heapq.heappush(pq, currInt)
                curr += 1

            while pq:
                length, currX, currY = pq[0]
                if currX <= num and num <= currY:
                    res[num] = length
                    break

            if not pq:
                res[num] = -1

        return [ res[i] for i in queries ]


