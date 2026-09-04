class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        longest_sequence = 1
        current_sequence = 1
        nums = sorted(list(set(nums)))

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                current_sequence += 1
                if current_sequence > longest_sequence:
                    longest_sequence = current_sequence
            else:
                current_sequence = 1
            
        
        return longest_sequence


        