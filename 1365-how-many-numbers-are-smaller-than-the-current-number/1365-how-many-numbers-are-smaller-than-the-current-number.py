class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sort_nums = sorted(nums)
        save = {}
        for i ,x in enumerate(sort_nums):
            if x not in save:
                save[x] = i
        return [save[num] for num in nums]