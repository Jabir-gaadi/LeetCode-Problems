class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        nums_len = len(nums)
        for i in range(nums_len - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = nums_len - 1
            while (left < right):
                total = nums[left] + nums[right] + nums[i]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res
        