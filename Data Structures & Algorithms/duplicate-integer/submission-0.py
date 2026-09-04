class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = {}
        for num in nums:
            if seen_nums.get(num, 0) > 0:
                return True
            else:
                seen_nums[num] = seen_nums.get(num,0) + 1
        
        return False

        