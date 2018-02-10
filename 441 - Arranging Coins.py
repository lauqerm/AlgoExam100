import math
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        sq = math.sqrt(n * 2)
        sqx = sq - (sq % 1)
        print(sqx)
        while True:
            tst = sqx * (sqx + 1) // 2
            if tst > n:
                sqx -= 1
            else:
                break
        return int(sqx)