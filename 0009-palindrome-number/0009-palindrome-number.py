class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return list(map(int, str(x))) == list(map(int, str(x)))[::-1]