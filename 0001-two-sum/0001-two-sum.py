class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(0, len(nums)):
            my_map[nums[i]] = i
        for num in nums:
            search = target - num
            if search in my_map:
                ans1 = my_map[search]
                ans2 = nums.index(num)
                if ans1!=ans2:
                    return ans1, ans2