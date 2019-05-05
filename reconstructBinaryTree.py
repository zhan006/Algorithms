'''given two strings one of which contains binary tree values that are pre_ordered  and another in_ordered
   reconstruct the original tree and make traversal in post_order
'''



preorder = "ABCDEFGHI"
inorder = "CBEDFAGIH"
pre2 = "GDAFEMHZ"
ino2 = "ADEFGHMZ"
pre3 = "ADCEFGHB"
ino3 = "CDFEGHAB"


def reorder(pre, ino):
    if len(pre) == 1:
        return NodeTree(pre)
    root = NodeTree(value=pre[0])
    i = ino.index(root.value)
    if i < len(ino) - 1 and i > 0:
        inoleft = ino[:i]
        preleft = pre[1:len(inoleft) + 1]
        inoright = ino[i + 1:]
        preright = pre[len(inoleft) + 1:]
        root.left = reorder(preleft, inoleft)
        root.right = reorder(preright, inoright)
    elif i == 0:
        inoright = ino[1:]
        preright = pre[1:]
        root.left = None
        root.right = reorder(preright, inoright)
    else:
        inoleft = ino[:i]
        preleft = pre[1:]
        root.left = reorder(preleft, inoleft)
        root.right = None
    return root


def preorder_visit(treenode):
    if not treenode == None:
        print(treenode.value)
        preorder_visit(treenode.left)
        preorder_visit(treenode.right)


def inorder_visit(treenode):
    if not treenode == None:
        inorder_visit(treenode.left)
        print(treenode.value)
        inorder_visit(treenode.right)


def postorder_visit(treenode):
    if not treenode == None:
        postorder_visit(treenode.left)
        postorder_visit(treenode.right)
        print(treenode.value)


class NodeTree:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


if __name__ == '__main__':
    head = reorder(preorder, inorder)
    #head2 = reorder(pre2,ino2)
    #head3 = reorder(pre3, ino3)
    #to test if the tree is right
    #preorder_visit(head)
    #inorder_visit(head)
    postorder_visit(head)
    #postorder_visit(head2)
    #postorder_visit(head3)
