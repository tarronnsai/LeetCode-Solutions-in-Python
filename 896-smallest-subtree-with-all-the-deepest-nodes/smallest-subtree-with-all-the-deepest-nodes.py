# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # This function returns (max_depth_of_subtree, best_node)
        def postOrder(node, depth):
            if not node:
                return depth, None
            
            left_depth, left_node = postOrder(node.left, depth + 1)
            right_depth, right_node = postOrder(node.right, depth + 1)
            
            # If both subtrees have the same max depth, 
            # this node is the potential LCA for deepest nodes
            if left_depth == right_depth:
                return left_depth, node
            
            # If left is deeper, the result must be in the left subtree
            if left_depth > right_depth:
                return left_depth, left_node
            
            # If right is deeper, the result must be in the right subtree
            return right_depth, right_node

        # Start recursion from root at depth 0
        _, result_node = postOrder(root, 0)
        return result_node

#tarronnsaiadabala