class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        def backtrack(curr, i):
            ans.append(list(curr))

            for k in range(i, len(nums)):
                if i != k and nums[k] == nums[k-1]:
                    continue
                curr.append(nums[k])
                backtrack(curr, k + 1)
                curr.pop()
            

        backtrack([], 0)

        return ans