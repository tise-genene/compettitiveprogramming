def rearrangeWithNeighbors(self, nums):
        
    def swap(curr_idx, nxt_idx):
        nums[curr_idx], nums[nxt_idx] = nums[nxt_idx], nums[curr_idx]
        
    arrSize = len(nums)
    
    for i in range(1, arrSize -1):
        prev, cur, nxt = nums[i-1], nums[i], nums[i+1]

        if prev < cur < nxt or prev > cur > nxt:
            swap(i+1, i)
            
    return nums
