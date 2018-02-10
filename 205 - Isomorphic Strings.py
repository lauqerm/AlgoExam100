class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c = {}
        d = {}
        dic = ""
        for j in range(0, 256):
            dic += chr(j)
        flag = True
        for i in range(0, len(s)):
            if not s[i] in c:
                if t[i] in dic:
                    c[s[i]] = t[i]
                    dic = dic.replace(t[i], "-")
                else:
                    flag = False
            else:
                if not (c[s[i]] == t[i]):
                    flag = False
        print(c)
        print(dic)
        return flag