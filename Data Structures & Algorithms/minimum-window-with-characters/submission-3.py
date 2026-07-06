class Solution:
    def minWindow(self, s: str, t: str):
        if t == "": return ""
        countT, window = {}, {}

        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        have, need = 0, len(countT)
        res = [-1, -1]
        res_length = float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < res_length:
                    res = [l, r]
                    res_length = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_length != float("inf") else ""


        