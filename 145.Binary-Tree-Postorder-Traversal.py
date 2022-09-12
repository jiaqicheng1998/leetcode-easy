# Given the root of a binary tree, return the 
# postorder traversal of its nodes' values.
#这是你visit每一个node之后，确认右边没有东西了，你再appen到res里面
#所以最上面的root在最后
#         100
#       /     \
#     20      200
#   /   \      /  \
# 10     30   150  300
# 顺序是 10 30 20 150 300 200 100

def postorderTraversal(root):
    res = []

    def postorder(root):
        if not root:
            return
        postorder(root.left)
        postorder(root.right)
        res.append(root.val)
    
    postorder(root)
    return res

def postorderTraversalIt(root):
    res = []
    stack = [(root, False)]

    while stack:
        node, flag = stack.pop()
        if node:
            if flag:
                res.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return res
