class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < temp:
                old_temp, old_i = stack.pop()
                ans[old_i] = i - old_i
            
            stack.append([temp, i])
        return ans
    
# O(1) Memory solution
    
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * n
        hottest = 0

        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            if temp >= hottest:
                hottest = temp
                continue
            
            days = 1
            while temperatures[i + days] <= temp:
                days += ans[i + days]
            
            ans[i] = days
        return ans
