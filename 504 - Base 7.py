class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num *= -1
            s = "-"
        elif num == 0:
            return "0"
        else:
            s = ""
        d = ""
        while num > 0:
            d = str(num % 7) + d
            num //= 7
        #print(d)
        s += d
        return s