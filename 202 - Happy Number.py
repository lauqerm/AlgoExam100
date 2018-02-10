class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = []
        while True:
            r = 0
            while n > 0:
                r += (n % 10) * (n % 10)
                n //= 10
            n = r
            #print(n)
            if n == 1:
                return True
            if r in d:
                return False
            d.append(r)