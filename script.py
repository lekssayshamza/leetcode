class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head

    while(current):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev



head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)

current = head

while(current):
    print(current.val)
    current = current.next

print()

head = reverseList(head)

current = head

while(current):
    print(current.val)
    current = current.next