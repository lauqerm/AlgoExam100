class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        carry = 1
        for c in range(len(digits) - 1, -1, -1):
            #print(digits[c])
            v = digits[c] + carry
            digits[c] = v % 10
            carry = v // 10
            #print(digits[c])
        if carry == 1:
            digits = [1] + digits
        return digits