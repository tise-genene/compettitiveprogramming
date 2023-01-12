import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                count=count+1
                temp=a[j]
                a[j]=a[j + 1]
                a[j + 1]=temp
                
        
    print('Array is sorted in '+str(count) + ' swaps.')
    print('First element: ' + str(a[0]))
    print('Last element: ' + str(a[len(a)-1]))
    return

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
