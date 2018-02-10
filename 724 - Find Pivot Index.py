class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        sl = 0
        sr = sum(nums[1:])
        for i in range(0, len(nums)):
            #print(i, sl, sr)
            if sl == sr:
                return i
            sl += nums[i]
            if i + 1 == len(nums):
                sr = 0
            else:
                sr -= nums[i + 1]
        return -1