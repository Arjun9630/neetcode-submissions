class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set(nums)
        longest = 0

        for num in seen:
            if num-1 not in seen:
                length = 1
                while num+1 in seen:
                    length += 1
                    num += 1
                
                longest = max(length, longest)

        return longest