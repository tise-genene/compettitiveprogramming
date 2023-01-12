def domino_pilling(m,n):
    if(1 < m<= 16 and 1 < n <= 16 ):
        max_piece = (m * n) // 2
        return max_piece
    else:
        return -1

m = int(input("Enter the m value: "))
n = int(input("Enter the n value: "))
print(domino_pilling(m, n))
