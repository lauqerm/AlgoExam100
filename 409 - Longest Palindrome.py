from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        r = 0
        flag = 0
        for i in c:
            if c[i] % 2 == 0:
                r += c[i]
            else:
                r += (c[i] - 1)
                flag = 1
        return r + flag