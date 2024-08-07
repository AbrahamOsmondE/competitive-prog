class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = 0
        currEnd = 0
        ans = 0
        for i in range(len(nums) - 1):
            currMax = max(currMax, nums[i] + i)

            if i == currEnd:
                currEnd = currMax
                ans += 1
        return ans
        