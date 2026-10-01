class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_dict = {}
        for i, num in enumerate(nums):
            left = target - num
            if left in my_dict:
                return [i, my_dict[left]]
            my_dict[num] = i