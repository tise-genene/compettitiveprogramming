class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ls, i = list(range(1, n + 1)), 0
        while len(ls) > 1:
            i = (i + k - 1) % len(ls)
            ls.pop(i)
        return ls[0]
