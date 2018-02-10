class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        mx = 0
        sm = 0
        for i in range(0, k):
            #print(nums[i])
            sm += nums[i]
        mx = sm
        #print(sm)
        for i in range(1, len(nums) - k + 1):
            sm = sm - nums[i - 1] + nums[i + k - 1]
            if sm > mx:
                mx = sm
            #print(sm)
            #print(nums[i:i + k:])
            #mx = max(mx, sum(nums[i:k + i:]))
        return mx / k