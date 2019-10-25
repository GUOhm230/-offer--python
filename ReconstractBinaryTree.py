"""
功能：重建二叉树。给定前序遍历和中序遍历，建立一颗二叉树。后输出其头结点
想法：二叉树中最常用的操作思想就是递归。
当前前序序列的的第一个值是这颗二叉树的根，
在中序遍历中的找到该节点后记录其位置，对以该节点位置为分隔线的子序列进行递归求解
"""


class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None


def reconstract_binarytree(pre, tin):
    # 会一直到空节点，要注意代码健壮性
    if not pre:
        return None
    root_val = pre[0]
    root = BinaryTree(root_val)
    for i in range(len(tin)):
        if tin[i] == root_val:
            break
    root.lchild = reconstract_binarytree(pre[1:i+1], tin[:i])
    # 注意在切片时是到末尾指向的前一个，中间用冒号分隔，不用逗号隔开
    root.rchild = reconstract_binarytree(pre[i+1:], tin[i+1:])
    return root


# 中序遍历二叉树
def preorder(root):
    if root:
        print(root.val)
        preorder(root.lchild)

        preorder(root.rchild)


print(reconstract_binarytree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6]))