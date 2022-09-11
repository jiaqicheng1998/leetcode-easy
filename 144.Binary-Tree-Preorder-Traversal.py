# Given the root of a binary tree, return 
# the preorder traversal of its nodes' values.

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
