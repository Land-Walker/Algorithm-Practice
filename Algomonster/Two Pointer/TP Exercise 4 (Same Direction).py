# LeetCode 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Original Code
def remove_nth_from_end(head, n):
    slow, fast = head, head
    count = 0
    for x in range(n):
        fast = fast.next
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

# Fixed Code with hint
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    slow, fast = dummy, dummy
    for x in range(n):
        fast = fast.next
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

"""
Notes

TP/Same Direction/Fixed Gap
Invariant: the gap between the pointers

Why I got wrong at the first place & What I did to fix?


"""