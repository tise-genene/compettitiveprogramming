def removeKdigits(self, num: str, k: int) -> str:
    ans = []

    for i in num:
        while k and len(ans) > 0 and ans[-1] > i:
            k -= 1
            ans.pop()
        ans.append(i)
    while k:
        k -= 1
        ans.pop()
        
    ans = "".join(ans).lstrip("0")

    return ans if ans else "0"
