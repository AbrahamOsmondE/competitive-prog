class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        counter = Counter(t)
        req = len(counter)

        sett = set(list(t))
        filtered = [(i, s[i]) for i in range(len(s)) if s[i] in sett]

        l,r = 0,0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        while r < len(filtered):
            char = filtered[r][1]
            window_counts[char] = window_counts.get(char, 0) + 1

            if window_counts[char] == counter[char]:
                formed += 1


            while l <= r and formed == req:
                char = filtered[l][1]

                end = filtered[r][0]
                start = filtered[l][0]
                length = end - start + 1
                if ans[0] > length:
                    ans = (length, start, end)
                
                window_counts[char] -= 1
                if window_counts[char] < counter[char]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

            
