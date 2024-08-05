class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        curr = []

        def isPalindrome(string):
            left = 0
            right = len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start=0):
            if start == len(s):
                ans.append(list(curr))
                return
            
            for i in range(start, len(s)):
                part = s[start:i+1]

                if isPalindrome(part):
                    curr.append(part)
                    backtrack(i+1)
                    curr.pop()
        backtrack()
        return ans




        
        