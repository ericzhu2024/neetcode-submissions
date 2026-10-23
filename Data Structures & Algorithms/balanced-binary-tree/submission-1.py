# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node):
            if not node:
                return (True, 0)
            left, l_depth = dfs(node.left)
            right, r_depth = dfs(node.right)
            if not (left and right) or abs(l_depth - r_depth) > 1:
                return (False, 0)
            return (True, max(l_depth, r_depth) + 1)
        
        return dfs(root)[0]
            