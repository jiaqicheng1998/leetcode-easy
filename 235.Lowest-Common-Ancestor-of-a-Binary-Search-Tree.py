# Given a binary search tree (BST), find the lowest common ancestor (LCA)
#  node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor
#  is defined between two nodes p and q as the lowest node in T that has both 
#  p and q as descendants (where we allow a node to be a descendant of itself).”


# if there is a split between between the two nodes, then it would be the LCA

def lowestCommonAncestor(root, p, q):
    cur = root

    while cur: #get it execute forever until we find the result
        #case we need to go down the right subtree
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
            # case we need to go down the left subtree
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur 
            #a split occurs of found the equal edge case