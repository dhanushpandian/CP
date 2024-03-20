class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Step 1: Traverse list1 to reach the (a-1)th node
        prev_a = None
        cur = list1
        for _ in range(a):
            prev_a = cur
            cur = cur.next
        # Step 2: Traverse list1 to reach the bth node
        node_b = cur
        for _ in range(b - a + 1):
            node_b = node_b.next
        # Step 3: Traverse list2 to reach the last node
        last_node_list2 = list2
        while last_node_list2.next:
            last_node_list2 = last_node_list2.next
        # Step 4: Link the (a-1)th node to the head of list2
        if prev_a:
            prev_a.next = list2
        else:
            list1 = list2
        # Step 5: Link the last node of list2 to the node after the bth node of list1
        last_node_list2.next = node_b
        
        return list1
