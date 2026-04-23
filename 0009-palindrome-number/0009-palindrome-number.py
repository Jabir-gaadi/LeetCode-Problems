class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = str(x)
        return res == res[::-1]