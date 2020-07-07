class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return head
        
        length = 1
        
        curr = head
        
        while(curr.next):
            length+=1
            curr = curr.next
        
        k=k%length
        curr.next = head
        
        for i in range(length-k-1):
            head = head.next
        
        last = head
        head = head.next
        last.next = None
        
        return head
        
        
        
        