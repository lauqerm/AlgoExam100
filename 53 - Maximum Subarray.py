class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        msf = 0
        meh = 0
        for i in nums:
            meh = meh + i
            if meh < 0:
                meh = 0
            if msf < meh:
                msf = meh
        msg = max(nums)
        if msf == 0:
            return msg
        else:
            return msf