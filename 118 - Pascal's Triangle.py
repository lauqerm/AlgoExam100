class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = [1]
        d = []
        for i in range(1, numRows + 1):
            d.append(a[:])
            a = map(lambda x, y: x + y, [0] + a, a + [0])
        return d