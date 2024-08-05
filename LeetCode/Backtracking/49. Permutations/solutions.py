class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def backtrack(curr, seen):
            if len(curr) == len(nums):
                ans.append(list(curr))
                return
            
            for i in nums:
                if i in curr:
                    continue
                curr.append(i)
                seen.add(i)
                backtrack(curr, seen)
                curr.pop()
                seen.remove(i)

        backtrack([], set())
        return ans