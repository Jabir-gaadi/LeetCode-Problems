class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        list_len = len(numbers)
        end = list_len - 1
        while start < end:
            total = numbers[start] + numbers[end]
            if total == target:
                return [start+1, end+1]
            if total > target:
                end -= 1
            else:
                start += 1
        return []