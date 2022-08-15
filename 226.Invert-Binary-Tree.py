def invertTree(root):
    if not root: #如果没有root
        return None 
    
    right = self.invertTree(root.right) #开始recursion
    left = self.invertTree(root.left)
    root.left = right #交换位置
    root.right = left
    return root

def invertTree_it(root):
    if not root:
        return None

    queue = []
    while queue:
        current = queue.pop(0)
        current.left, current.right = current.right, current.left

        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)
        
        return root