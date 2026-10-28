# link: https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False

head = ListNode(10)
head.next = ListNode(20)
# head.next.next = head

print(hasCycle(head))