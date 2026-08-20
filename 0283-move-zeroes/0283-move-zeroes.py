class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        j = 0
        for i in range(nums_len):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
