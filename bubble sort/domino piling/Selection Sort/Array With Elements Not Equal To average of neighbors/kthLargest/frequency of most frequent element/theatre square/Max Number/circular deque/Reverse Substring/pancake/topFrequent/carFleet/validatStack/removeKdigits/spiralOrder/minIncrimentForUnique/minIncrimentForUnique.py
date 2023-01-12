def minIncrementForUnique(self, nums: List[int]) -> int:
    nums.sort()
    count = 0

    for i in range(1, len(nums)):
        cur = nums[i]
        prev = nums[i-1]
        if(prev >= cur ):
            nums[i] = prev + 1
            count += prev - cur + 1
            
    return count 
