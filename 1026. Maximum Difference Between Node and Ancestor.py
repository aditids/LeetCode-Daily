# 1026. Maximum Difference Between Node and Ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, maxv, minv):
            if not root:
                return abs(maxv-minv)
            maxv = max(maxv, root.val)
            minv = min(minv, root.val)
            left = dfs(root.left, maxv, minv)
            right = dfs(root.right, maxv, minv)
            return max(left, right)
        return dfs(root, float('-inf'), float('inf'))
        # Time complexity - O(n)