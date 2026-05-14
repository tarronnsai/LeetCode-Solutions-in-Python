# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []

        # Helper function to calculate subtree sums
        def get_sum(node):
            if not node:
                return 0
            
            # Current subtree sum is node val + left child sum + right child sum
            current_sum = node.val + get_sum(node.left) + get_sum(node.right)
            subtree_sums.append(current_sum)
            return current_sum

        # 1. Get the total sum (which is the sum of the root's subtree)
        total_sum = get_sum(root)
        
        # 2. Find the maximum product
        max_prod = 0
        for s in subtree_sums:
            # The two parts after cutting are 's' and 'total_sum - s'
            product = s * (total_sum - s)
            if product > max_prod:
                max_prod = product
        
        return max_prod % (10**9 + 7)

#tarronnsaiadabala