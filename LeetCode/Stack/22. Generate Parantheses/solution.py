# 1. Recursive approach
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        answer = []
        for left_count in range(n):
            for left_string in self.generateParenthesis(left_count):
                for right_string in self.generateParenthesis(n - 1 - left_count):
                    answer.append("(" + left_string + ")" + right_string)
        return answer
    
#2. Backtracking approach
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(string, left, right):
            if len(string) == n * 2:
                ans.append("".join(string))
                return
            
            if left < n:
                string.append("(")
                backtrack(string, left + 1, right)
                string.pop()
            if right < left:
                string.append(")")
                backtrack(string, left, right + 1)
                string.pop()
            

        backtrack([], 0, 0)
        return ans
        