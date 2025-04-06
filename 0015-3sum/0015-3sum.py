class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i=0
        n=len(nums)
        while(i<n-2):
            j=i+1
            k=n-1
            target=-1*nums[i]    
            while(j<k):
                # print(i, j, k)
                tSum = nums[j] + nums[k]
                # print(tSum, target)
                if tSum==target:
                    # print("break", i, j, k)
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while(j<n and nums[j]==nums[j-1]):
                        j+=1
                    k-=1
                    while(k>0 and nums[k]==nums[k+1]):
                        k-=1
                elif tSum>target:
                    k-=1
                else:
                    j+=1            
            # if j<k:
            #     ans.append([nums[i], nums[j], nums[k]])
            i_next=i+1
            while(i<n-2 and nums[i_next]==nums[i]):
                i=i_next
                i_next=i+1 
            i+=1
        return ans