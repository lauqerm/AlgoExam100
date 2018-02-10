class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num == 0:
            return False
        while num % 30 == 0:
            num /= 30
        while num % 15 == 0:
            num /= 15
        while num % 10 == 0:
            num /= 10
        while num % 6 == 0:
            num /= 6
        while num % 5 == 0:
            num /= 5
        while num % 3 == 0:
            num /= 3
        while num % 2 == 0:
            num /= 2
        return num == 1