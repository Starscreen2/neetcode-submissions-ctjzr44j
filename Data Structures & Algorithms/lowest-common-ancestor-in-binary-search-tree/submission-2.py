# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        current = root

        while current:
            if q.val < current.val and p.val < current.val:
                current = current.left
            elif q.val > current.val and p.val > current.val:
                current = current.right
            else:
                return current

