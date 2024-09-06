# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        d={i:1 for i in nums}
        node=ListNode(0)
        node.next=head
        cur=node
        while cur.next:
            if cur.next.val in d:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return node.next