class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False
        match = re.match(r'(.*?)(?:\1)*$', s)
        word = match.group(1)
        if len(s) // len(word) == 1:
            return False
        return True