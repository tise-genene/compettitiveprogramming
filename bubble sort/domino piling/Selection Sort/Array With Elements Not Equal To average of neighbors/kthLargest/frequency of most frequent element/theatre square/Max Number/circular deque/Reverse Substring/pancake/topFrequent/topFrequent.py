import collections
import heapq

def topKFrequent(self, nums, k):
    dic = dict(collections.Counter(nums))
    heap = []

    for key, val in dic.items():
        if len(heap) == k:
            heapq.heappushpop(heap, (val,key))
        else:
            heapq.heappush(heap, (val,key))
            
    return [y for x,y in heap]
