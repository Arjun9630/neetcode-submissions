class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        output_sequence = []
        value = 1
        if not nums:
            return 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                if num-1 in seen:
                    value += 1
                else:
                    if value != 1:
                        output_sequence.append(value)
                        value = 1
        output_sequence.append(value)
        return max(output_sequence)
        