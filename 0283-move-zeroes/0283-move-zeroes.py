class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        for i in range(0,len(nums)):
            if nums[i] == 0:
                for j in range(i+1,len(nums)):
                    if nums[j]!= 0 :
                        nums[i],nums[j]=nums[j],nums[i]
                        break
                

            if i == len(nums):
                return

               

        return nums