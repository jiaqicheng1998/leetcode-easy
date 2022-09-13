# Given the root of a binary tree, check whether it 
# is a mirror of itself (i.e., symmetric around its center).

def isSymmetric(root):
    
    def mirror(t1, t2):
        if (t1 is None and t2 is None):
            return True
        if (t1 is None or t2 is None):
            return False
        
        return (t1.val == t2.val) and mirror(t1.left, t2.right) and mirror(t1.right, t2.left)
    return mirror(root.left, root.right)
                

