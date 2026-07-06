class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights) - 1
        while left != right:
            area = min(heights[left], heights[right]) * abs(left - right)
            if max_water == 0:
                max_water = area

            if max_water != 0 and max_water < area:
                max_water = area

            if heights[right] < heights[left]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                left += 1
        return max_water