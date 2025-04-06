class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxm_area = 0
        while left<right:
            heightOfContainer = min(height[left], height[right])
            width = right-left
            current_area = heightOfContainer * width
            maxm_area = max(maxm_area, current_area)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return maxm_area
        