class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(0, len(s)):
            res += roman[s[i]]
            if i == 0:
                continue
            if (s[i] == 'V' or s[i] == 'X') and s[i -1] == 'I':
                res -= 2
            elif  (s[i] == 'L' or s[i] == 'C') and s[i -1] == 'X':
                res -= 20
            elif (s[i] == 'D' or s[i] == 'M') and s[i -1] == 'C':
                res -= 200
        return res