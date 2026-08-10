class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = (len(nums)//2) + 1
        map = {}
        res = 0
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
            if map[num] == target:
                return num
        return res