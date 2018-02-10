class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        leng = len(nums)
        return max(nums[leng - 1] * nums[leng - 2] * nums[leng - 3], nums[leng - 1] * nums[0] * nums[1])