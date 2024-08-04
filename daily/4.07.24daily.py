# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Creating new LinkedList for answer
class Solution:
    def mergeNodes(self, head) :
        a=[]
        # print(head.val)
        s=0
        while head.next:
            if head.next.val != 0:
                s+= head.next.val
            else:
                a.append(s)
                s=0
            head.next=head.next.next
        d=ListNode(0)
        cur=d
        for i in a:
            cur.next=ListNode(i)
            cur=cur.next
        return d.next
            

#optimized code

class Solution:
    def mergeNodes(self, head) :
        dummy = ListNode(0)
        dummy.next = head
        slow = head
        fast = head.next
        s = 0
        
        while fast:
            if fast.val != 0:
                s += fast.val
            else:
                slow.val = s
                s = 0
                if fast.next:  # Move slow pointer only if there's more to process
                    slow = slow.next
            fast = fast.next
        
        slow.next = None  # Ensure the next pointer of the last node is None
        
        return dummy.next