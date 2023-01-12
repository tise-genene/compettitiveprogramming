def maxFrequency(self, nums, k):
    nums.sort()
    sum, i, freq = 0, 0, 0
    for j in range(len(nums)):

        sum += nums[j]
        while nums[j]*(j-i+1) > sum+k:
            sum -= nums[i]
            i = i+1
        freq = max(freq, j-i+1)

    return freq
