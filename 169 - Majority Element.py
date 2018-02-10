from collections import Counter
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        l = len(nums)
        for i in c:
            if c[i] * 2 > l:
                return i