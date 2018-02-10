class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ['0']
        astr = list(s)
        for i in astr:
            if i == '(':
                a.append(i)
            elif i == '[':
                a.append(i)
            elif i == '{':
                a.append(i)
            elif i == ')':
                if a.pop() == '(':
                    null = 1
                else:
                    return False
            elif i == ']':
                if a.pop() == '[':
                    null = 1
                else:
                    return False
            elif i == '}':
                if a.pop() == '{':
                    null = 1
                else:
                    return False
        if len(a) == 1:
            return True
        else:
            return False