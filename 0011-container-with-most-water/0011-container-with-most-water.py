class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")
        l, r = 0, len(height)-1
        while(l<r):
            max_area = max((r-l)*min(height[l],height[r]), max_area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
        

# [1,8,6,2,5,4,8,3,7]
#. 0,1,2,3,4,5,6,7,8