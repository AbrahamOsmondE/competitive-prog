class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        mono_stack = []
        for i, h in enumerate(chain([0], heights, [0])): # append zero heights at both ends
            while len(mono_stack) > 0 and mono_stack[-1][1] > h:
                prev_i, prev_height = mono_stack.pop()
                left = mono_stack[-1][0]
                current_area = (i - left - 1) * prev_height
                ans = max(ans, current_area)
            
            mono_stack.append([i, h])
        
        return ans