#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        car=0
        while(l1 or l2 or car):
            if l1:
                a = l1.val
            else:
                a = 0
            if l2:
                b = l2.val
            else:
                b = 0
            c=a+b+car
            car=c//10
            ans=c%10

            cur.next=ListNode(ans)
            cur=cur.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next

