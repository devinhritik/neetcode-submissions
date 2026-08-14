class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        maxcount = []
        for n in nums:
            count[n] = 1 + count.get(n,0)
        result = sorted(count , key=count.get, reverse = True)
        return result[:k]

