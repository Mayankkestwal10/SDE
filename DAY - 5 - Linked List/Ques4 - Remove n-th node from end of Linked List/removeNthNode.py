# Method - 1 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = self.countNode(head)
        
        if(size==0):
            return head
        
        if(size==1):
            head = None
            return head
        
        reach = size - n - 1
        if(reach<0):
            it = head
            head = head.next
            it.next = None
            return head
        
        it = head
        temp = 0
        
        while(it and temp!=reach):
            temp+=1
            it = it.next
        
        f = it.next
        it.next = it.next.next
        f.next = None
        
        return head
        
        
    def countNode(self, head):
        cnt = 0
        it = head
        while(it):
            cnt+=1
            it = it.next
        return cnt


# Method - 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        
        for i in range(n):
            fast = fast.next
            
        if fast==None:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return head