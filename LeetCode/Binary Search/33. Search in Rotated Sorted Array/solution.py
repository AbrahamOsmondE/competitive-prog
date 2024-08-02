class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        mid = 0
        while left <= right:
            if nums[-1] > nums[0]:
                break
            mid = (left + right) // 2

            if nums[mid] < nums[mid - 1]:
                break
            elif nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1

        num_rotated = mid

        left = 0
        right = len(nums) - 1
        n = len(nums)

        while left <= right:
            mid = (left + right) // 2
            index = (mid + num_rotated) % n

            if nums[index] == target:
                return index
            elif nums[index] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
            