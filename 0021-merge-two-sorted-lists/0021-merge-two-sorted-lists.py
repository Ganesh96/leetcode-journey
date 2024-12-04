# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        curr3 = None
        prev = None
        head = None

        # Iterate while either list has elements
        while curr1 or curr2:
            smaller = ListNode()

            # Choose the smaller value and create a new node
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    smaller.val = curr1.val
                    curr1 = curr1.next
                else:
                    smaller.val = curr2.val
                    curr2 = curr2.next
            elif curr1:  # If only list1 has elements
                smaller.val = curr1.val
                curr1 = curr1.next
            else:  # If only list2 has elements
                smaller.val = curr2.val
                curr2 = curr2.next

            # Link the new node to the previous node and update prev and head
            if prev:
                prev.next = smaller
            else:
                head = smaller
            prev = smaller

        return head