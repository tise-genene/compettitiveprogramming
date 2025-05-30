class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        def helper(arr,n,i):
            l=2*i+1
            r=2*i+2

            if l<n and arr[l]>arr[i]:
                largest=l
            else: largest=i

            if r<n and arr[r]>arr[largest]:
                largest=r
            if largest!=i:
                arr[i],arr[largest]=arr[largest],arr[i]
                helper(arr,n,largest)
        helper(arr,n,i)


    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        for i in range(int(n/2)-1,-1,-1):
            self.heapify(arr,n,i)
        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            self.heapify(arr,i,0)
