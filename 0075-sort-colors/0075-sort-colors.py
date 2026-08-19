class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        i = 0
        j = i + 1
        while i < nums_len - 1:
            if nums[i] > nums[j]:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i = 0
                j = i + 1
            else:
                i += 1
                j =  i + 1
        return nums