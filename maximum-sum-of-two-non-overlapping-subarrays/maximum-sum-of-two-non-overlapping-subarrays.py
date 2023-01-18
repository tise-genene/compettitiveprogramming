class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n=len(nums)
        result,curMax,secondmax = -inf ,-inf,-inf
        secondstart,secondend = [0]*n , [0]*n   
        curSum,firstsum,secondsum = 0,0,0
       
        i = n-1
        while i>=0:
            curSum += nums[i]
            if i+secondLen < n : 
                curSum -= nums[i + secondLen]
            if i+ secondLen<= n :
                curMax = max(curMax, curSum)
                secondstart[i] = curMax
            i-=1      
    
        for i in range(n):
            secondsum += nums[i]
            if i+1 > secondLen : 
                secondsum -= nums[i - secondLen]
            if i+1 >= secondLen :
                secondmax = max(secondmax, secondsum)
                secondend[i] = secondmax
            firstsum += nums[i]  
            if i +1> firstLen :
                firstsum -= nums[i - firstLen]
            if i+1 >= firstLen:
                leftsum = 0 if i - firstLen < secondLen- 1 else secondend[i - firstLen]
                rightsum =  secondstart[i + 1] if i + 1 + secondLen - 1 < n else 0
                temp = firstsum + max(leftsum,rightsum)
                result  = max(result,temp  )
     
  
        return result 
