class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sett = set()
        
        ans = []
        for i in range(len(nums) - 2):
            target = nums[i] * -1
            twoSum = {}
            for j in range(i + 1, len(nums)):
                if nums[j] in twoSum and tuple(sorted([nums[i], nums[j], target - nums[j]])) not in sett:
                    ans.append([nums[i], nums[j], target - nums[j]])
                    sett.add(tuple(sorted([nums[i], nums[j], target - nums[j]])))
                twoSum[target - nums[j]] = 1
        return ans
    
# 3sum no sort