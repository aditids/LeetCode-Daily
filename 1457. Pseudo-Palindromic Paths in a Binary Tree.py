# 1457. Pseudo-Palindromic Paths in a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def check(arr):
            odd = 0
            for i in arr:
                if i%2!=0: odd+=1
                if odd>1: return 0
            return 1

        def dfs(root, count):
            if not root: return 0
            count[root.val] += 1
            if not root.left and not root.right:
                result = check(count)
            else:
                result = dfs(root.left, count) + dfs(root.right, count)
            count[root.val]-=1
            return result
    
        return dfs(root, [0]*10)       