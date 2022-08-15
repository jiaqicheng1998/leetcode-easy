# Given the roots of two binary trees p and q, write a function 
# to check if they are the same or not.

# Two binary trees are considered the same if they are structurally 
# identical, and the nodes have the same value.

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:

# Input: p = [1,2,1], q = [1,1,2]
# Output: false

def isSameTree(p, q):
    if not p and not q: return True
    if not p: return False
    if not q: return False
        
    stack1 = [p]
    stack2 = [q]
    values1 = [p.val]
    values2 = [q.val]

    while stack1:
        curr = stack1.pop()
        if curr.right:
            stack1.append(curr.right)
            values1.append(curr.right.val)
        else:
            values1.append(None)
        if curr.left:
            stack1.append(curr.left)
            values1.append(curr.left.val)
        else:
            values1.append(None)

    while stack2:
        curr = stack2.pop()
        if curr.right:
            stack2.append(curr.right)
            values2.append(curr.right.val)
        else:
            values2.append(None)
        if curr.left:
            stack2.append(curr.left)
            values2.append(curr.left.val)
        else:
            values2.append(None)

    if len(values1) != len(values2):
        return False
    else:
        for i in range(len(values1)):
            if values1[i] != values2[i]:
                return False
    return True





