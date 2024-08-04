class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def backtrack(curr, index):
            if index == len(nums):
                return


            curr.append(nums[index])
            backtrack(curr, index+1)
            ans.append([i for i in curr])
            curr.pop()
            backtrack(curr, index + 1)
        
        backtrack([], 0)

        ans.append([])
        return ans