#Consecutive Characters

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = None
        res = 1
        count = 0
        for i in range(len(s)):
            if last == None:
                last = s[i]
                count = 1
            elif last == s[i]:
                count += 1
                res = max(count,res)
            else:
                count = 1
                last = s[i]
        return res