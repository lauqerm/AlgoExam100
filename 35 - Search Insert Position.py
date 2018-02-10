class Solution:
    arr = []
    v = 0
    def search(self, l, r):
        t = self.arr[(l + r) // 2]
        if r - l == 1:
            #print("Not Found")
            return l
        if self.v > t:
            #print("Left", (l + r) // 2, r)
            return self.search((l + r) // 2, r)
        if self.v < t:
            #print("Right", l, (l + r) // 2)
            return self.search(l, (l + r) // 2)
        if self.v == t:
            #print("Found")
            return (l + r) // 2 - 1
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.arr = [nums[0] - 1] + nums
        #print(self.arr)
        self.arr = self.arr + [nums[len(nums) - 1] + 1]
        #print(self.arr)
        self.v = target
        return self.search(0, len(self.arr) - 1)