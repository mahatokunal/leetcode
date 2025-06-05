class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n):
            if nums[i]==0:
                nums[i]=-1
            
        prefix_sum = 0
        hashMap = {}
        ans=0

        for i in range(0, n):
            prefix_sum += nums[i]
            if prefix_sum==0:
                ans = max(ans, i+1)
            elif prefix_sum in hashMap:
                ans = max(ans, i-hashMap[prefix_sum])
            else:
                hashMap[prefix_sum] = i
        
        return ans

        # 0,1
        # -1,0

        # 0,1,0
        # -1,0,-1

        # [ 0,1,1,1,1,1,0,0,0
        # [-1,0,1,2,3,4,3,2,1]
        #    0,1,2,3,4,5,6,7,8