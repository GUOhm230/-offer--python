"""
功能：二叉树中序遍历的下一个节点
分析：二叉树中序遍历是左根右，当前节点的下一个节点一定不会出现在当前节点的左子树上
因为该节点的左子树节点只可能出现在其前驱上，
所以当前节点的下一个节点只可能是该节点的父节点或者右子树上
思想：1.假如当前节点没有右子树，则依次向上查找其父节点，如果当前节点是其父节点的左子节点则返回其父节点
否则，依次查找其父节点，直至当前节点是父节点的左子树
2.如果当前节点有右子树，且当前节点的右子节点没有左子树，则返回其右子节点，
否则，依次遍历当前节点右子树的左子节点至该节点没有左子节点，返回该节点
"""
class TreeNode:
    def __init__(self):
        self.val = None
        self.lchild = None
        self.rchild = None
        self.father = None


def tree_next(node_p):
    if node_p.rchild == None:
        while node_p.father != None:
            if node_p.father.lchild == node_p:
                return node_p.father
            else:
                node_p = node_p.father
    else:
        if node_p.rchild.lchild == None:
            return node_p.rchild
        else:
            node_p = node_p.rchild
            while node_p.lchild != None:
                return node_p.lchild


#  二叉判定树的绘制
def constract_tree(treelist, start, end):
    if end >= start:
        root = TreeNode()
        mid = int((start+end)/2)
        root.val = treelist[mid]
        root.lchild = constract_tree(treelist, start, mid-1)
        root.rchild = constract_tree(treelist, mid+1, end)
    else:
        root = None
    return root


if __name__ == '__main__':
    treelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = constract_tree(treelist, 0, len(treelist)-1)
    node_p = root.lchild.rchild
    print(tree_next(node_p).val)
    print(int((2+3)/2))








