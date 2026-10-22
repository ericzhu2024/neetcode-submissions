# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    

        def helper(cur: Optional[TreeNode]):
            if cur is None:
                return 
            helper(cur.left)
            helper(cur.right)
            temp = cur.left
            cur.left = cur.right
            cur.right = temp
        helper(root)
        return root