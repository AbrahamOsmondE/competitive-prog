class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        dicti = collections.defaultdict(int)
        ans = 0
        while right < len(s):
            char = s[right]
            if dicti[char] == 0:
                dicti[char] = 1
            else:
                while dicti[char] == 1:
                    curr = s[left]
                    dicti[curr] = 0
                    left += 1
                dicti[char] = 1
            right += 1
            ans = max(ans, right - left)
        return ans
        