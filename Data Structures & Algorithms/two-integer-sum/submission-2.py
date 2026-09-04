class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            try:
                j = nums.index(diff)
            except:
                continue

            if i!=j:
                return sorted([i, j])
        