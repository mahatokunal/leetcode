class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, prefixSum = 0, 0
        diffHashmap = {0: 1}

        for i in range(0,n):
            prefixSum += nums[i]
            diff = prefixSum-k
            if  diff in diffHashmap:
                ans = ans + diffHashmap[diff]
            diffHashmap[prefixSum] = diffHashmap.get(prefixSum, 0) + 1

        return ans

# 0,1,2
# 1,1,1
# 1,2,3
# 
# 0,1,2
# 1,2,3
# 1,3,6
# 