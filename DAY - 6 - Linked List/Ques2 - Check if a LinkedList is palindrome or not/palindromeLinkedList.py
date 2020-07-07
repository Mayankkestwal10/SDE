# Method 1 - Stack

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        
        it = head
        while(it):
            stack.append(it.val)
            it = it.next
            
        while(head):
            if(head.val!=stack.pop()):
                return False
            
            head = head.next
            
        return True

# Method 2 - Reversing

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        current = slow
        
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        
        while(head and prev):
            if(head.val!=prev.val):
                return False
            head = head.next
            prev = prev.next
            
        return True
        