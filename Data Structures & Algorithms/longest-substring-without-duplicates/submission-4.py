class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = set()
        max_s = 0
        left = 0

        for right, ch in enumerate(s):

            while ch in seen:
                seen.remove(s[left])
                left += 1

            seen.add(ch)

            max_s = max(max_s, right - left + 1)

        return max_s