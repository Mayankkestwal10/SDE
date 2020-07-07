class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        
        if(curr is None):
            return head
        
        while(curr.next):
            if(curr.val==curr.next.val):
                new = curr.next.next
                curr.next = None
                curr.next = new
            else:
                curr = curr.next
                
        return head