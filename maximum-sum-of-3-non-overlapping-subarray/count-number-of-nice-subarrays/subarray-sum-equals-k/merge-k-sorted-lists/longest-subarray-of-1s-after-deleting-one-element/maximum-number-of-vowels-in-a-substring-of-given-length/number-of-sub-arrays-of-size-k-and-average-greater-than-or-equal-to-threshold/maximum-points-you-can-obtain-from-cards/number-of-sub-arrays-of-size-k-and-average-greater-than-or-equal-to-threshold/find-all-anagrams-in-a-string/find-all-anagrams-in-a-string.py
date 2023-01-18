class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        ls = len(s)
        ans = []
        dictionaryS =defaultdict(int)
        dictionaryP = defaultdict(int)
        if lp > ls:
            return []
        for i in range(len(p)):
            dictionaryP[p[i]] += 1
            dictionaryS[s[i]] += 1
       
        j = 0
        if dictionaryP==dictionaryS:
            ans = [0]
        else:
            ans = []
        for i in range(lp, ls):
            dictionaryS[s[i]] += 1
            dictionaryS[s[j]] -= 1
            if dictionaryS[s[j]] == 0:
                del dictionaryS[s[j]]
            j += 1
            
            if dictionaryS == dictionaryP:
                ans.append(j)
           
          
        return ans
            
                
