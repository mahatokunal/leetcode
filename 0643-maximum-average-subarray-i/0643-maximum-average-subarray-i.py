class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum=0
        for i in range(0, k):
            sum += nums[i]
        max_sum = sum
        print(max_sum, sum)
        for i in range(k, n):
            sum = sum - nums[i-k] + nums[i]
            max_sum = max(sum, max_sum)
            print(max_sum, sum)
        return max_sum/k