import numpy as np
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        e = []
        c = [0 for j in range(0, 26)]
        u = [0 for j in range(0, 26)]
        if len(s) < len(p):
            return []
        else:
            for i in range(0, len(p)):
                c[ord(p[i]) - ord('a')] += 1
                u[ord(s[i]) - ord('a')] += 1
            print(c)
            print(u)
            if np.array_equal(c, u) == True:
                e.append(0)
            for i in range(1, len(s) - len(p) + 1):
                u[ord(s[i + len(p) - 1]) - ord('a')] += 1
                u[ord(s[i - 1]) - ord('a')] -= 1
                flag = 1
                for k in range(0, 26):
                    if not(c[k] == u[k]):
                        flag = 0
                        break
                if flag == 1:
                    e.append(i)
        return e
            
        