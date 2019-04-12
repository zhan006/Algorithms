#given two string one of which is post_order traversal from a binary tree while another in_order,
#reoder the binary tree based on those two string
def post_reorder(post, ino):
    root = NodeTree()
    if post == "":
        pass
    else:
        root.value = post[-1]
        index = ino.index(root.value)
        root.left = post_reorder(post[:index], ino[:index])
        root.right = post_reorder(post[index:-1], ino[index + 1:])
    return root