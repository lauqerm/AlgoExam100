class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 1
        r = 1
        while True:
            r = (r + num / r) / 2
            #print(r)
            if abs(l - r) <= 1:
                k = int(r)
                if k * k == num:
                    return True
                if (k + 1) * (k + 1) == num:
                    return True
                if (k - 1) * (k - 1) == num:
                    return True
                return False
            l = r