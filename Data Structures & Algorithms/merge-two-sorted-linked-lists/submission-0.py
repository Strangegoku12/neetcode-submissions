# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the anchor for the new list
        dummy = ListNode(0)
        current = dummy
        
        # 2. Loop while both lists still have nodes to compare
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # Link the smaller node
                list1 = list1.next    # Move list1 pointer forward
            else:
                current.next = list2  # Link the smaller node
                list2 = list2.next    # Move list2 pointer forward
                
            current = current.next    # Move our main list pointer forward
            
        # 3. If one list runs out, instantly attach the remaining part of the other list
        current.next = list1 if list1 else list2
        
        # Return the actual head of the merged list (skipping the dummy node)
        return dummy.next
