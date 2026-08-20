class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i + 1
        nums_len = len(nums)
        while i < nums_len - 1:
            j = i + 1
            if nums[i] == nums[j]:
                nums.pop(i)
                i -= 1
            nums_len = len(nums)
            i += 1
        # nums = [num for num in nums if num != -1]
        return len(nums)