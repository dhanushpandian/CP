
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap={None:None}
        cur=head
        while(cur):
            cp= Node(cur.val)
            hashmap[cur]=cp
            cur=cur.next
        
        cur=head
        while(cur):
            cp=hashmap[cur]
            cp.next=hashmap[cur.next]
            cp.random=hashmap[cur.random]
            cur=cur.next
        
        return hashmap[head]

# if __name__=="__main__":
#     head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
