class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        first = nums.index(min(nums))
        second = nums.index(max(nums))
        min_idx = min([first, second])
        max_idx = max([first, second])
        from_front = max_idx + 1
        from_end = len(nums) - min_idx
        third_option = len(nums) - max_idx
        third_choice = third_option + min_idx + 1
        return min([from_end, from_front, third_choice])
