class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        
        def backtrack(currSum=target, curr=[], start=0):
            if currSum == 0:
                ans.append(list(curr))
                return

            if currSum < 0 or start == len(candidates):
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                curr.append(candidates[i])
                backtrack(currSum - candidates[i], curr, i + 1)
                curr.pop()
        backtrack()
        return ans
