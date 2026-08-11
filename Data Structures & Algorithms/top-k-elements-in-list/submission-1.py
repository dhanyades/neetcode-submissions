class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        
        map = dict(sorted(map.items(), key=lambda x: x[1], reverse=True))
        keys = list(map.keys())
        return keys[:k]