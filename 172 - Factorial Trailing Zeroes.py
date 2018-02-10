class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        mul = 5
        while True:
            a = n // mul
            mul *= 5
            if a < 1:
                break
            cnt += a
        return cnt