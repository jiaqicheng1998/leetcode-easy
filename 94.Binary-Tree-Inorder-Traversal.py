# Given the root of a binary tree, return the inorder 
# traversal of its nodes' values
#这是你visit每一个node之后，当你确认左边没有东西了，你就append到res里面
# 是整个tree从左到右的一个呈现
#         100
#       /     \
#     20      200
#   /   \      /  \
# 10     30   150  300
# 顺序是 10 20 30 100 200 150 300 

#recursive solution
# def inorderTraversal(root):
#     res = []

#     def inorder(root):
#         if not root:
#             return
#         inorder(root.left)
#         res.append(root.val)
#         inorder(root.right)
    
#     inorder(root)
#     return res


#iterative solution
def inorderTraversal(root):
    res = []
    stack = []
    cur = root
    
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res 

     