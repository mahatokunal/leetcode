class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for (i, num) in enumerate(nums):
            search = target - num
            if search in my_map:
                return my_map[search], i
            my_map[num] = i