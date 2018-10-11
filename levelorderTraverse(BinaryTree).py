# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        nodes = []
        while queue:
            tmp_nodes = []
            tmp_vals = []
            for node in queue:
                tmp_vals.append(node.val)
                if node.left:
                    tmp_nodes.append(node.left)
                if node.right:
                    tmp_nodes.append(node.right)

            nodes.append(tmp_vals)
            queue = tmp_nodes

        return nodes