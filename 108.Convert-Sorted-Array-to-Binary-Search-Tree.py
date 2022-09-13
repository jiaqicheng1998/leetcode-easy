# Given an integer array nums where the elements are sorted 
# in ascending order, convert it to a height-balanced binary 
# search tree.

# A height-balanced binary tree is a binary tree in which 
# the depth of the two subtrees of every node never differs 
# by more than one.

def sortedArrayToBST(nums):

    def helper(l, r):
        if l > r:
            return None
        
        m = (l + r) // 2
        root = TreeNode(nums[m])
        root.left = helper(l, m - 1)
        root.right = helper(m + 1, r)
        return root
    
    return helper(0, len(nums) - 1)
