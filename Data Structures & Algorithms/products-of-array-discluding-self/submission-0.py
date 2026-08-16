class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        prods = [1] * len(nums)
        for i in range(len(nums)):
            prods[i] *= pre
            pre *= nums[i]

        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            prods[i] *= suf
            suf *= nums[i]
        
        return prods