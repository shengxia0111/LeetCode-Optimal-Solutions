# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversalIter(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #顺序遍历二叉树迭代版
        if not root:
            return []
        node,stack=[],[]
        while 1:
            #遍历所有左节点，直到没有左节点
            while not root:
                #将已遍历的左节点放入node
                node.append(root.val)
                #栈中放入当前节点，准备进入下一节点
                stack.append(root)
                root=root.left
                #如果栈中没有节点，则说明现在只有右节点
                if not stack:
                    return node
            #释放上一节点
            node=stack.pop()
            #进入右节点
            root=node.right

    def preorderTraversalRecursive(self,root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        self.traversal(root, nodes)
        return nodes

    def traversal(self, root, nodes):
        if not root:
            return
        nodes.append(root.val)
        self.traversal(root.left, nodes)
        self.traversal(root.right, nodes)
