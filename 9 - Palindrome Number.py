class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        cnt = 0
        n = x
        k = 0
        if(n < 0):
            return False
        while n > 0:
            k = n % 10
            cnt = cnt * 10 + k
            n = (n - k) / 10
        print(x)
        print(cnt)
        if(x == cnt):
            return True
        else:
            return False