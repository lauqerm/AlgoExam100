class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = max(nums)
        kq = nums.index(m1)
        nums.pop(kq)
        if nums == []:
            return kq
        m2 = max(nums)
        #print(m1, m2)
        if m1 >= m2 * 2:
            return kq
        else:
            return -1