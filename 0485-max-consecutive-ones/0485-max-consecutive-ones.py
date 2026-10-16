class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maxi = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxi = max(count, maxi)
                count = 0
        if nums[-1] == 1 and maxi < count:
            maxi = count
        return maxi