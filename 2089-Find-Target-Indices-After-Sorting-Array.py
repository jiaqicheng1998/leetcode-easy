nums = [1,2,5,2,3]
target = 5

def targetIndices(nums, target):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if nums[i] == target:
            res.append(i)
    return res

print(targetIndices(nums, target))