class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        list1 = []

        while current != None:
            list1.append(current.val)
            current = current.next
        
        list1.sort()

        current = ans = None

        for i in list1:
            new = ListNode(i)

            if ans == None:
                ans = new
                current = ans
            else:
                current.next = new
                current = new
        
        return ans