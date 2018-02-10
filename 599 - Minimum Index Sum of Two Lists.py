class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        s = set(list1).intersection(list2)
        d = {}
        for i in s:
            d[i] = 0
            d[i] += list1.index(i) + list2.index(i)
        mid = min(d.values())
        r = []
        for i in d:
            if d[i] == mid:
                r.append(i)
        return r