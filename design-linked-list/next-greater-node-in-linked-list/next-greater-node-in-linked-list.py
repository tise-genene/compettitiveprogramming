#Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        length = 0
        temp = head
        d={}
        
        while temp:
            d[length]= temp.val
            temp = temp.next
            length+=1
        key = list(d.keys())
        value = list(d.values())

        print(d)
        print(key)
        print(value)
        stk = []
        result = [0 for _ in range(length)]
     
        while head:
            while stk and head.val > stk[-1]:  
                data = stk.pop()
                print(data)
                print(head.val)
                idx=value.index(data)      
                result[key[idx]]=head.val
            stk.append(head.val)
            head = head.next
        
        
        return 
