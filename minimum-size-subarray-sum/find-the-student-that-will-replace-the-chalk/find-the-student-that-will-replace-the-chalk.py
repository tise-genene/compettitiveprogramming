class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum = 0
        for num in chalk:
            sum+=num
        i = k%sum
        if i == 0:
             return 0
        for j in range(len(chalk)):
            i -= chalk[j]
            if i <= -1:
                return j
            
