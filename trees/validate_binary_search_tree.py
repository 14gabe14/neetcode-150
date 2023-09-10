# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root)[0]
        
    def recurse(self, node: Optional[TreeNode]):
        if node.left:
            is_valid, min_left, max_left = self.recurse(node.left)

            if not is_valid or min_left >= node.val or max_left >= node.val:
                return (False, 0, 0)

            min_val = min_left
        else:
            min_val = node.val

        if node.right:
            is_valid, min_right, max_right = self.recurse(node.right)

            if not is_valid or min_right <= node.val or max_right <= node.val:
                return (False, 0, 0)

            max_val = max_right
        else:
            max_val = node.val

        return (True, min_val, max_val)

        
        


