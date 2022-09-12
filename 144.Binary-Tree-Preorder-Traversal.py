# Given the root of a binary tree, return 
# the preorder traversal of its nodes' values.

#每当你到一个node里面，你先把node的value放到result里面去
#所以它正好是你visit每一个node的顺序
#         100
#       /     \
#     20      200
#   /   \      /  \
# 10     30   150  300
# 顺序是 100 20 10 30 200 150 300

def preorderTraversal(root):
    res = []

    def preorder(root):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
    
    preorder(root)
    return res

def preorderTraversalIter(root):
    res = []
    if not root:
        return res
    stack = [root]

    while stack:
        cur = stack.pop()
        if cur:
            res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return res
