class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1]*n
        suffix = nums[n-1]
        for i in range(1, n):
            out[i] = out[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            out[i] = out[i] * suffix
            suffix = suffix * nums[i]
        return out