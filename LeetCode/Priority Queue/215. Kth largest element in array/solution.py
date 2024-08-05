class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = []
        for i in nums:
            if len(ans) == k:
                heapq.heappushpop(ans, i)
            else:
                heapq.heappush(ans, i)
        return min(ans)
        