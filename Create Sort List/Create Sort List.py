class Solution(object):
    def sortList(self, head):
        result=[]
        current=head
        newhead=head
        while current:
            result.append(current.val)
            current=current.next
        result.sort()
        i=0
        while newhead:
            newhead.val=result[i]
            newhead=newhead.next
            i+=1
        return head
