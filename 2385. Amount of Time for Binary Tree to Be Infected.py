# Definition for a binary tree node.
# Amount of Time for Binary Tree to Be Infected

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        visited = set()
        q = deque([start])
        count = -1

        def dfs(root):
            if not root: return
            if root.left: 
                graph[root.left.val].append(root.val)
                graph[root.val].append(root.left.val)
            if root.right:
                graph[root.right.val].append(root.val)
                graph[root.val].append(root.right.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        while q:
            n = len(q)
            count+=1
            for i in range(n):
                curr = q.popleft()
                visited.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        q.append(neighbor)
        return count