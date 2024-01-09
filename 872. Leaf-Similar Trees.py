# 872. Leaf-Similar Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.a1 = []
        def dfs(root):
            if not root: return
            if root.left is None and root.right is None:
                self.a1.append(root.val)
                return
            dfs(root.left)
            dfs(root.right)
        dfs(root1)
        self.a2 = self.a1
        self.a1 = []
        dfs(root2)
        return self.a1==self.a2
