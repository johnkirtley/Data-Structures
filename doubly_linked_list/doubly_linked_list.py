"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.head.prev = None
            self.tail.prev = self.head
            self.tail.next = None
            self.length += 1
            return self.head.value
        else:
            old_head = self.head
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return old_head.value

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):

        if self.head is None:
            return
        elif self.length == 1:
            removed_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_head.value
        else:
            old_head = self.head
            new_head = self.head.next
            self.head = new_head
            self.length -= 1
            return old_head.value
    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.head.prev = None
            self.tail = new_node
            self.head.next = self.tail
            self.tail.next = None
            self.length += 1
            return self.head.value
        else:
            old_tail = self.tail
            self.tail.next = new_node
            self.tail = new_node
            new_node.prev = old_tail
            self.length += 1
            return old_tail.value

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return
        elif self.head is self.tail:
            removed_tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_tail.value
        else:
            new_tail = self.tail.prev
            removed_tail = self.tail
            self.tail = new_tail
            self.length -= 1
            return removed_tail.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):

        if self.head is None and self.tail is None:
            self.head = node
            self.head.prev = None
            self.tail = node
            self.tail.prev = self.head
            self.tail.next = None
            self.head.next = self.tail
            return
        elif self.head is node and self.tail is node:
            return self.head.value
        else:

            current = self.head
            while current is not None:
                if current == node:
                    moved_node = current
                    prev_node = current.prev
                    next_node = current.next

                    prev_node.next = next_node

                    old_head = self.head
                    self.head.prev = moved_node
                    self.head = moved_node
                    self.head.next = old_head
                    return
                current = current.next

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):

        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):

        self.length -= 1

        if self.head is None:
            return

        if self.head is self.tail:
            removed_node = self.head
            self.head = None
            self.tail = None
            return removed_node.value

        if self.head == node:
            removed_node = self.head
            new_head = self.head.next
            self.head = new_head
            self.head.prev = None
            return removed_node.value
        elif self.tail == node:
            removed_node = self.tail
            new_tail = self.tail.prev
            self.tail = new_tail
            self.tail.next = None
            return removed_node.value

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        if self.head is None:
            return
        else:
            max_value = self.head.value

            current = self.head
            while current is not None:
                if current.value > max_value:
                    max_value = current.value
                current = current.next
            return max_value

    def print_list(self):
        arr = []
        if self.head is None and self.tail is None:
            return
        else:
            current = self.head
            while current is not None:
                arr.append(current)
                current = current.next

        for i in range(len(arr)):
            print(arr[i].value)
