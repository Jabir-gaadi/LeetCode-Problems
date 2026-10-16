class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for x, y in enumerate(range(n, len(nums))):
            res.append(nums[x])
            res.append(nums[y])
        return res