class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def backtrack(total, curr, start):
            if total == 0:
                ans.append([_ for _ in curr])
                return
            if total < 0:
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(total - candidates[i], curr, i)
                curr.pop()
            
        backtrack(target, [], 0)

        return ans



        