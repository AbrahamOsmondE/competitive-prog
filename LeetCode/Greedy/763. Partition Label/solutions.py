class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        arr = [[-1, -1] for _ in range(26)]
        for i, char in enumerate(s):
            charIndex = ord(char) - ord('a')
            if arr[charIndex][0] != -1:
                arr[charIndex][1] = i
            else:
                arr[charIndex][0] = i
        arr = [[i,j] if j!=-1 else [i,i] for i,j in arr if i!=-1]
        arr.sort()
        stack = []
        for interval in arr:
            if len(stack) == 0:
                stack.append(interval)
                continue
            
            if stack[-1][1] > interval[0]:
                stack[-1][1] = max(stack[-1][1], interval[1])
            else:
                stack.append(interval)
        
        return [j - i + 1 for i,j in stack]