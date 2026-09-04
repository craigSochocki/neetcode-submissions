class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        res = dict(sorted(counts.items(), key= lambda item: item[1], reverse=True))
        return [key for key,value in res.items()][:k]
