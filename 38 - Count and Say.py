class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        n -= 1
        st = "1x"
        st2 = ""
        while n > 0:
            cnt = 0
            slot = ""
            for c in st:
                if slot == "":
                    slot = c
                if slot == c:
                    cnt += 1
                else:
                    st2 += str(cnt) + slot
                    slot = c
                    cnt = 1
            #print(st2)
            st = st2 + "x"
            if not n == 1:
                st2 = ""
            n -= 1
        return st2
                    