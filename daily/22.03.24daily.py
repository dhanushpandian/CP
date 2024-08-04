#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        cur=head
        a=[]
        while cur:
            a.append(cur.val)
            cur=cur.next
        return a==a[::-1]