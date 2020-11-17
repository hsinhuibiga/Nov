#Mirror Reflection

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        m, n = q, p
        while m % 2 == 0 and n % 2 == 0:
            m, n = m / 2, n / 2
        if m % 2 == 0 and n % 2 == 1:
            return 0
        elif m % 2 == 1 and n % 2 == 1:
            return 1
        elif m % 2 == 1 and n % 2 == 0:
            return 2