#Minimum Cost to Move Chips to The Same Position

class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        counter = collections.Counter(position)

        cnt = 0
        for pos in position:
            if (pos % 2 == 0):
                cnt += 1
        return min(cnt, len(position) - cnt)