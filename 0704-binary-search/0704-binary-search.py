class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            print("mid = ", mid)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                print("b")
                r= mid-1
            else:
                print("c")
                l=mid+1
        return -1