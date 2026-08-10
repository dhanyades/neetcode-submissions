class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,num in enumerate(nums):
            find = target - num
            if find in map:
                if map[find]!= i:
                    return [map[find], i]
                continue
            map[num] = i

