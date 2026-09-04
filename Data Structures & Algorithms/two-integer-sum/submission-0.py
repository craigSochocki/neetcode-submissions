class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            lhs = nums[i]
            for j in range(len(nums)):
                rhs = nums[j]
                if i != j and lhs + rhs == target:
                    return sorted([i, j])

        