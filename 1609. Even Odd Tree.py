# 1609. Even Odd Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]        
        nidx = 0
        while q:
            n = len(q)
            nval = 0
            for i in range(n):
                k = q.pop(0)
                if i == 0:
                    if nidx%2==0 and (k.val%2==0):
                        return False
                    if nidx%2!=0 and (k.val%2!=0):
                        return False
                    nval = k.val
                elif nidx%2==0 and (k.val%2==0 or k.val<=nval):
                    return False
                elif nidx%2!=0 and (k.val%2!=0 or k.val>=nval):
                    return False
                nval = k.val
                
                if k.left:
                    q.append(k.left)
                if k.right:
                    q.append(k.right)
            nidx+=1
        return True 