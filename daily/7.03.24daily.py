#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        cur=head
        c=1
        while cur.next:
            cur=cur.next
            c+=1
        c=int(c/2)+1
        i=1
        cur=head
        while i<c and cur.next:
            i+=1
            cur=cur.next
        return cur
    
#using Floyds Algo
class Solution:
    def middleNode(self, head):
        if not head:
            return None
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow