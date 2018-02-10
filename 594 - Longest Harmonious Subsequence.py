class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if not i in d:
                d[i] = 1
            else:
                d[i] += 1
        m = 0
        v1 = 0
        v2 = 0
        for i in d:
            if i - 1 in d:
                n = d[i] + d[i - 1]
                if n > m:
                    m = n
                    v1 = i
                    v2 = i - 1
            if i + 1 in d:
                n = d[i] + d[i + 1]
                if n > m:
                    m = n
                    v1 = i
                    v2 = i + 1
        return m