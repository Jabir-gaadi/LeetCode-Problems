from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        dict_score = Counter(nums)
        i = 0
        for i in range(k):
            tmp = max(dict_score, key=dict_score.get)
            res.append(tmp)
            dict_score.pop(tmp)
        return res