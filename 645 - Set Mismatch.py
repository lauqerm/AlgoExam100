class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num2 = set(nums)
        t = sum(nums) - sum(num2)
        m = len(nums)
        return [t, m * (m + 1) // 2 - sum(num2)]