# Given a non-empty array of integers nums, every element appears 
# twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity 
# and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]
# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:

# Input: nums = [1]
# Output: 1

def singleNumber(nums):
    d = {}
    for i in nums:
        if i in d:
            del d[i]
        else:
            d[i] = 1
    return list(d.keys())[0]

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))