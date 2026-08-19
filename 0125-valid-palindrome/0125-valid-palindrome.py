class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_list = [char.lower() for char in s if char.isalpha() or char.isdigit()]
        return (str_list == str_list[::-1])