# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key<root.val :
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right = self.deleteNode(root.right,key)
        else: # Equal condition
            #No child
            if root.left is None and root.right is None:
                return None
            #One child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            #2 child
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right,successor.val)
        return root