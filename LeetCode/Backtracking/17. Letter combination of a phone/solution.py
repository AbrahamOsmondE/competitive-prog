class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) == 0:
            return []
        ans = []
        curr = []
        def backtrack(index=0):
            if index == len(digits):
                ans.append("".join(curr))
                return
            
            num = digits[index]

            for char in letters[num]:
                curr.append(char)
                backtrack(index+1)
                curr.pop()
        backtrack()
        return ans