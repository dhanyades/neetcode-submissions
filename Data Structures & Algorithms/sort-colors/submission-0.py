class Solution:
    def sortColors(self, nums: List[int]) -> None:
        white = 0
        b = True
        blue = 0
        c = True

        while b:
            if 1 in nums:
                nums.remove(1)
                white +=1
            else:
                b = False
        while c:
            if 2 in nums:
                nums.remove(2)
                blue +=1
            else:
                c = False
        
        for i in range(white):
            nums.append(1)
        for i in range(blue):
            nums.append(2)
        """
        Do not return anything, modify nums in-place instead.
        """
        