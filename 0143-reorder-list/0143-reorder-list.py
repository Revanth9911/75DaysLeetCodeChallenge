class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        """
        Do not return anything, modify head in-place instead.
        """

        # Edge case
        if not head or not head.next:
            return
        
        # 🔹 Step 1: Find middle (slow & fast)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 🔹 Step 2: Reverse second half
        prev = None
        curr = slow.next
        slow.next = None   # break the list
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 🔹 Step 3: Merge both halves
        first, second = head, prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2