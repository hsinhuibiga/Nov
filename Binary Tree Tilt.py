#Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sums = 0
        self.postOrder(root)
        return self.sums

    def postOrder(self, root):
        if not root:
            return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        self.sums += abs(left - right)
        return left + right + root.val