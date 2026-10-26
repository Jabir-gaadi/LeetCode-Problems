class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sort_nums = sorted(nums)
        save = {}
        for i ,x in enumerate(sort_nums):
            if x not in save:
                save[x] = i
        # save = {x:i for x,i in enumerate(sort_nums) if x not in save}
        return [save[num] for num in nums]