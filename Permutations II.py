#Permutations II

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, res, [])
        return res

    def helper(self, nums, res, path):
        if not nums and path not in res:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.helper(nums[:i] + nums[i + 1:], res, path + [nums[i]])
