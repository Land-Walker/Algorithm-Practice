# LeetCode 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    return slow

"""
Notes

TP/SameDirection/RelativeSpeed

Invariant: Distance between pointers is meaningful

Since I was not sure about how linked list works in python,
used AI on Algomonster. 
- seems more straightforward than C++
"""