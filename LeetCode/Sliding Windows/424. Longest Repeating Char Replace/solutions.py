class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = collections.defaultdict(int)
        max_count = 0
        left = 0
        ans = 0
        for right in range(len(s)):
            char = s[right]
            counter[char] += 1

            max_count = max(max_count, counter[char])
            is_valid = right - left + 1 - max_count <= k
            if not is_valid:
                left_char = s[left]
                counter[left_char] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans
            