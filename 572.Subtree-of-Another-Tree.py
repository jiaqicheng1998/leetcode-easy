# Given the roots of two binary trees root and subRoot, return true if 
# there is a subtree of root with the same structure and node values 
# of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in 
# tree and all of this node's descendants. The tree tree could also be 
# considered as a subtree of itself.

# Example 1:

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:

# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# def isSubtree(root, subRoot):
#     if not root:
#         if not subRoot: 
#             return True
#         else:
#             return False
    
#     res = []

#     def isSameTree(p,q):
#         if not p and not q: return True
#         if not p: return False
#         if not q: return False

#         def getValues(treeRoot):
#             stack = [treeRoot]
#             values = [treeRoot.val]

#             while stack:
#                 curr = stack.pop()
#                 if curr.right:
#                     stack.append(curr.right)
#                     values.append(curr.right.val)
#                 else:
#                     values.append(None)
                
#                 if curr.left:
#                     stack.append(curr.left)
#                     values.append(curr.left.val)
#                 else:
#                     values.append(None)
            
#         values1 = getValues(p)
#         values2 = getValues(q)

#         if len(values1) != len(values2):
#             return False
#         else:
#             for i in range(len(values1)):
#                 if values1[i] != values2[i]:
#                     return False
#         return True

#     def dfs(root, subRoot):
#         if not root:
#             return False
#             res.append(False)
        
#         left = dfs(root.left, subRoot)
#         res.append(left)
#         right = dfs(root.right, subRoot)
#         res.append(right)

#         return isSameTree(root, subRoot)
    
#     dfs(root, subRoot)
#     return any(res)

# brute force: visit every single node in the root, does the tree match the subRoot tree
def isSubtree(s, t):
    if not t: return True
    if not s: return False

    if sameTree(s, t):
        return True
    
    return (isSubtree(s.left, t) or 
            isSubtree(s.right, t))


def sameTree(s, t):
    if not s and not t:
        return True
    
    if s and t and s.val == t.val:
        return (sameTree(s.left, t.left) and
                sameTree(s.right, s.right))
    
    return False

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False



    

        
                
