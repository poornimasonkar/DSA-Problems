class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            nums[i] += n * (nums[nums[i]] % n)
        for i in range(n):
            nums[i] //= n
        return nums
