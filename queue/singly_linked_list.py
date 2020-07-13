class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, value):
        self.next = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_tail(self):

        if not self.tail:
            return None

        if self.head is self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.next is not self.tail:
            current = current.next

        value = self.tail.value
        self.tail = current
        self.tail.next = None

        return value

    def contains(self, value):
        if not self.head:
            return False

        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def remove_head(self):
        if self.head is None:
            return

        if not self.head.next:
            head = self.head

            self.head = None
            self.tail = None

            return head.value

        value = self.head.value
        self.head = self.head.next

        return value

    def get_max(self):
        if not self.head:
            return

        max_value = self.head.value

        current = self.head
        while current is not None:
            if current.value > max_value:
                max_value = current.value

            current = current.next

        return max_value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, value):
        self.next = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_tail(self):

        if not self.tail:
            return None

        if self.head is self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.next is not self.tail:
            current = current.next

        value = self.tail.value
        self.tail = current
        self.tail.next = None

        return value

    def contains(self, value):
        if not self.head:
            return False

        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def remove_head(self):
        if self.head is None:
            return

        if not self.head.next:
            head = self.head

            self.head = None
            self.tail = None

            return head.value

        value = self.head.value
        self.head = self.head.next

        return value

    def get_max(self):
        if not self.head:
            return

        max_value = self.head.value

        current = self.head
        while current is not None:
            if current.value > max_value:
                max_value = current.value

            current = current.next

        return max_value
