def foo(nums):
    nums.sort()
    for i in range(len(nums) - 3, -1, -1):  #from the largest three numbers to the smallest three numbers, find triangle
        if nums[i] + nums[i+1] > nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0
