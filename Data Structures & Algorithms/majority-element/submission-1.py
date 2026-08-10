class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = (len(nums)//2) + 1
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
            if map[num] == target:
                return num
        return 0