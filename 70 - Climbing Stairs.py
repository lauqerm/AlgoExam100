class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        a = 1
        b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
            #print(a, b)
        return b