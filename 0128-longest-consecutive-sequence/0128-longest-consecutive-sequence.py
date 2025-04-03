class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq=0
        num_set = set(nums)
        for num in nums:
            if num-1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num+1 in num_set:
                    current_num = current_num + 1 
                    current_streak = current_streak + 1
                
                longest_seq = max(current_streak, longest_seq)
        return longest_seq
        