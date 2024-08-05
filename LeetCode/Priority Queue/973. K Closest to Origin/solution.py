class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        def distance(x, y):
            return (x**2 + y**2)
        
        if len(points) == k:
            return points
        
        for i, j in points:
            dist = distance(i,j)
            if len(ans) == k:
                heapq.heappushpop(ans, (-1 * dist, i, j))
            else:
                heapq.heappush(ans, (-1 * dist, i, j))
                
        
        return [[x, y] for _, x, y in ans]