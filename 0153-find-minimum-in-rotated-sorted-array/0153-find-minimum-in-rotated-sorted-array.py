class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[l]<=nums[r]:
            return nums[l]
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[l]<nums[mid]:
                l=mid
            elif nums[mid]<nums[r]:
                r=mid  