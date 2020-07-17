class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # check if list is empty
        if node is not None:
            # preserve current next_node in nxt_node variable
            nxt_node = node.next_node
            # replace next_node pointer with prev node
            node.next_node = prev

            # prev node is now current node
            prev = node
            # current node is now the next pointer
            node = nxt_node
            # recursively invoke reverse_list passing in node and prev which used to be
            # nxt pointer and current node
            self.reverse_list(node, prev)
        else:
            # else node head is prev node
            self.head = prev
