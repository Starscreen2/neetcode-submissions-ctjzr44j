class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        for num in range(len(nums)):
            if nums[l] == 0:
                nums.pop(l)
                nums.append(0)

            if nums[l] != 0:
                l+=1
            
        return nums