class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        slow = fast = A
        
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if(slow==fast):
                slow = A
                while(slow.next!=fast.next):
                    slow = slow.next
                    fast = fast.next
                    
                fast.next = None
                return A
                
        return A