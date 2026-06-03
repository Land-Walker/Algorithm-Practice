# LeetCode 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/

int middle_of_linked_list(Node<int>* head) {
    Node<int>* slow = head;
    Node<int>* fast = head;
    while (fast && fast->next) {
        fast = fast->next->next;
        slow = slow->next;
    }
    return slow->val;
}

"""
Notes

"""