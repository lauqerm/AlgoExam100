class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = re.sub(r'  *', ' ', s)
        s = s.strip()
        print(s)
        if s == "":
            return 0
        if s == " ":
            return 0
        return len(s.split(" "))