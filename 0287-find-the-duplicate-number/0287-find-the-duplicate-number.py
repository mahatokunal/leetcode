class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow==fast:
                return slow
        
# 1 3 4 2 2
# 