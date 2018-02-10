class Solution:
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = []
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        d.append(nums[0])
        d.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            d.append(0)
            d[i] = max(d[i - 2] + nums[i], d[i - 1])
        return d.pop();