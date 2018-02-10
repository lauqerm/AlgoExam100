from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        n = Counter(ransomNote)
        m = Counter(magazine)
        for i in n:
            if not i in m:
                return False
            if n[i] > m[i]:
                return False
        return True