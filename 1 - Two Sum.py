class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, c in enumerate(nums):
            d = target - c
            if d in nums and not(index == nums.index(d)):
                return [min(index, nums.index(d)), max(index, nums.index(d))]