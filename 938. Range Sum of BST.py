# 938. Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.rSum = 0
        def inorder(root):
            if not root: return
            elif low<=root.val<=high: 
                self.rSum+=root.val
            if root.val> low: inorder(root.left)
            if root.val< high: inorder(root.right)
            return 
        inorder(root)
        return self.rSum
        