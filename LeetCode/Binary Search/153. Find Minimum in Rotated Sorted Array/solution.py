class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        if nums[-1] > nums[0]:
            return nums[0]

        mid = 0
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[mid]