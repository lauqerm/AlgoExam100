class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = bin(num)
        #print(n)
        #print(n.count("0"))
        #print(num & (num - 1))
        return n.count("0") % 2 == 1 and not num & (num - 1)