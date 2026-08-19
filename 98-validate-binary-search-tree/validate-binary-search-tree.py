# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],min: Optional[int] = None, max: Optional[int] =None) -> bool:
        if root is None:
            return True
        if min is not None and root.val<=min:
            return False
        if max is not None and root.val>=max:
            return False
        return self.isValidBST(root.left,min,root.val) and self.isValidBST(root.right,root.val,max)

        