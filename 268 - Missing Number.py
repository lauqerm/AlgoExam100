class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        return m * (m + 1) // 2 - sum(nums)