def pancakeSort(self, arr):
   
    result=[]
    n=len(arr)

    while(n):
        pos = arr.index(n)+1
        result.append(pos)
        arr = arr[pos-1::-1] + arr[pos:]
        result.append(n)
        arr = arr[n-1::-1] + arr[n:]
        n -= 1

    return result
