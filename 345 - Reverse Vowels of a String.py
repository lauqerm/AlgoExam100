class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = 'aeiouAEIOU'
        if s == "":
            return ""
        st = list(s)
        l = -1
        fl = False
        r = len(s)
        fr = False
        while True:
            if not fl:
                l += 1
                if st[l] in vowel:
                    fl = True
            if not fr:
                r -= 1
                if st[r] in vowel:
                    fr = True
            if l >= r:
                break
            if fl and fr:
                st[r], st[l] = st[l], st[r]
                fl = False
                fr = False
            #print(s, l, r)
        return ''.join(st)