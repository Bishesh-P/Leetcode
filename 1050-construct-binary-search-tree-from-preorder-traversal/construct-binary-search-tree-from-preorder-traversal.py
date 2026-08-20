# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0
        def build(bound):
            if self.idx == len(preorder) or preorder[self.idx] >bound:
                return None
            node = TreeNode(preorder[self.idx])
            self.idx +=1
            node.left = build(node.val)
            node.right = build(bound)
            return node
        return build(float('inf'))
