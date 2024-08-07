class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('-inf')
        curr = 0
        summ = 0
        while curr < len(nums):
            summ += nums[curr]
            ans = max(ans, summ)

            if summ < 0:
                summ = 0
            curr += 1
        return ans