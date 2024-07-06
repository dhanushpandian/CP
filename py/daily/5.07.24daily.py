# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        a={}
        idx=1
        while head.next:
            a[idx]=(head.next.val)
            head.next=head.next.next
            idx+=1
        #print(a)
        if len(a) < 3:
            return [-1,-1]
        i=1
        b=[]
        while i<len(a)-1:
            if a[i] > a[i-1] and a[i] > a[i+1]:
                b.append(a[i])
            if a[i] < a[i-1] and a[i] < a[i+1]:
                b.append(a[i])
            i+=1
        print(b)
        x=max(b)
        y=min(b)
        for i in b:
            for j in b:
                z = abs(i-j)
                x=min(x,z)
                y=max(y,z)

        return [x,y]
    

