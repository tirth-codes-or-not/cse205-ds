class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        myset = set()
        current = headA

    
        while current.next != None:
            myset.add(current)
            current = current.next
        
        current = headB
        while current.next != None:
            if current in myset:
                return current 
            current = current.myset()
        return None