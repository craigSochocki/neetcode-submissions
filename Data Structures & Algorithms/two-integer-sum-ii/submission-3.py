class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers)

        while i < j - 1:
            if numbers[i] + numbers[j-1] > target:
                j -= 1
            elif numbers[i] + numbers[j-1] < target:
                i += 1
            else:
                return [i + 1, j]

