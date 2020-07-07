# Method 1 - Using length of Lists

'''
So the idea is :
1. to calculate the length of both the lists c1 and c2
2. Calculate absolute difference between the lengths i,e. d = abs(c1-c2)
3. Now determine which list is longer in length and iterate over it d nodes ahead doing so lead you to both lists having same number of nodes left to iterate.
4. Now start iterating both lists at the same time if the reference headA==headB matches just return headA or headB otherwise keep iteration till either any one of the list reaches null.
5. If in case no intersection is found just return None.
'''


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        c1 = self.countNode(headA)
        c2 = self.countNode(headB)
        
        d = abs(c1-c2)
        
        if(c1>c2):
            while(d!=0):
                d-=1
                headA =headA.next
            
        else:
            while(d!=0):
                d-=1
                headB =headB.next
                
        while(headA and headB):
            if(headA==headB):
                return headA
            
            headA = headA.next
            headB = headB.next
        
        return None
                

# Method 2 - Dictionary