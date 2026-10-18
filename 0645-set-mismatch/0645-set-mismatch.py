class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()
        nums_len = len(nums)
        seen = []
        res = []
        res.append(sum(nums) - sum(set(nums)))
        target = 1
        count = 1
        for i in range(nums_len):
            if target == nums[i]:
                target += 1
            if nums[i] == target:
                continue
        res.append(target)
        return res