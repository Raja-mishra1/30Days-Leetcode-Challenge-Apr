class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        s = head
        f = head
        
        while f is not None:
            if not f.next:
                break
            s = s.next
            f = f.next.next
            
        return s