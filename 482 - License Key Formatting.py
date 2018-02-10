class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace("-","").upper()
        u = []
        r = ""
        m = len(s) % K
        n = len(s) // K
        for i in range(0, m):
            r += s[i]
        if not r == "":
            u.append(r)
        t = m
        for i in range(0, n):
            r = ""
            for j in range(0, K):
                r += s[m + i * K + j]
            u.append(r)
        return "-".join(u)