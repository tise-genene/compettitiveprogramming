def maxOperations(self, nums, k):
    nums.sort()
    operations = 0
    i, j = 0, len(nums)-1
    while i < j:
        sums = nums[i] + nums[j]
        if sums == k:
            operations += 1
            i, j = i+1, j-1
        elif sums > k:
            j = j-1
        else:
            i = i+1
    return operations
