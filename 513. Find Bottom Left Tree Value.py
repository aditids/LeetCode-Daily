# 513. Find Bottom Left Tree Value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [root]
        while q:
            node = q.pop(0)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val


        # self.res = -inf
        # self.mcount = -inf
        # def dfs(root, count=0):
        #     if not root: return
        #     if not root.left and not root.right: 
        #         if count>self.mcount:
        #             self.mcount = count
        #             self.res = root.val
        #         return
        #     count+=1
        #     dfs(root.left,count)
        #     dfs(root.right,count)
            
        # dfs(root)
        # #print(self.res)
        # return self.res