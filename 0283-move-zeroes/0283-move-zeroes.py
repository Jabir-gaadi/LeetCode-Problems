class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        nums_len = len(nums)
        j = nums_len - 1
        while i < j:
            if nums[j] == 0:
                j -= 1
                continue
            if nums[i] != 0:
                i += 1
                continue
            tmp = i
            while tmp < j:
                nums[tmp], nums[tmp+1] = nums[tmp+1], nums[tmp]
                tmp += 1
            # i += 1
        return nums