"""
功能：二叉树中两节点的最近公共子节点
作者：郭辉铭。2019.10.29
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def lowestCommonAncestor(self, root, A, B):
        if (root is None or root == A or root == B):
            return root  # 若root为空或者root为A或者root为B，说明找到了A和B其中一个
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        if left and right:
            return root  # 若左子树找到了A，右子树找到了B，说明此时的root就是公共祖先
        if not left:  # 若左子树是none右子树不是，说明右子树找到了A或B
            return right
        if not right:  # 同理
            return left
        return None
