#Maximum Difference Between Node and Ancestor

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(root, max_v, min_v):
            if not root:
                return
            self.ans =  max(self.ans, abs(max_v - root.val), abs(min_v - root.val))
            max_v = max(max_v, root.val)
            min_v = min(min_v, root.val)
            dfs(root.left, max_v, min_v)
            dfs(root.right, max_v, min_v)

        dfs(root.left, root.val, root.val)
        dfs(root.right, root.val, root.val)

        return self.ans