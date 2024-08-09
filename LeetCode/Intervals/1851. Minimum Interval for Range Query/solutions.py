class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort(key=lambda i: (i[0], i[1]))
        queries = [(val, index) for index,val in enumerate(queries)]
        queries.sort(key=lambda i: i[0])
        pq = []
        ans = []
        curr = 0

        for num, i in queries:
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
                    ans.append(length)
                    break

            if not pq:
                ans.append(-1)
        
        while len(ans) < len(queries):
            ans.append(-1)
        
        res = [0 for _ in range(len(queries))]

        for i in range(len(queries)):
            actualIndex = queries[i][1]
            res[actualIndex] = ans[i]

        return res


