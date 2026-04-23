class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_index = 0
        for first in nums:
            second_index = 0
            for second in nums[1:]:
                second_index += 1
                if first_index == second_index:
                    continue
                if target == first + second:
                    return [nums.index(first), second_index]
            first_index += 1