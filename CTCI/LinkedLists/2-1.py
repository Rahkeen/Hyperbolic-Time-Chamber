""" Remove duplicates from an unsorted linked list

    FOLLOW UP: What if you wanted to use constant memory?
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def create_list_with_repeats():
    head = Node(1)
    curr = head
    for i in xrange(4):
        curr.next = Node(2)
        curr = curr.next

    curr.next = Node(3)
    return head

def create_list_no_repeats():
    head = Node(1)
    curr = head
    for i in xrange(2,6):
        curr.next = Node(i)
        curr = curr.next

    return head

def print_list(head):
    curr = head
    result = ''
    while curr:
        result += str(curr.val) + ' --> '
        curr = curr.next

    print result + 'x'

# Solutions

def remove_duplicates(head):
    if not head:
        return None

    curr = head
    prev = None
    visited = set()

    while curr:
        if curr.val in visited:
            prev.next = curr.next
        else:
            visited.add(curr.val)
            prev = curr

        curr = curr.next

def remove_duplicates_2(head):
    if not head:
        return None

    curr = head
    while curr:

        runner = curr.next
        prev = curr
        while runner:

            if runner.val == curr.val:
                prev.next = runner.next
            else:
                prev = runner

            runner = runner.next
        
        curr = curr.next


head = create_list_with_repeats()
# head = create_list_no_repeats()

print_list(head)
remove_duplicates_2(head)
print_list(head)
