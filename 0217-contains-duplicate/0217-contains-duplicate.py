from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = Counter(nums)
        return not(sum(nums_dict.values()) == len(set(nums)))
        