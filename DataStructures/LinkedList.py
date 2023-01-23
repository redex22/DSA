class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head) if head is not None else None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def get(self, index):
        curr_idx = 0
        current_node = self.head
        while current_node:
            if curr_idx == index:
                return current_node.value
            curr_idx += 1
            current_node = current_node.next
        raise IndexError("Value out of range")

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        return " -> ".join([str(node) for node in self])

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


if __name__ == "__main__":
    list1 = LinkedList(1)
    list1.append(2)
    list1.append(3)
    list2 = LinkedList()
    list2.append("Uno")
    list2.append("Dos")
    list2.append("Tres")
    print(list1)
    print(list2)
    print(len(list1), len(list2))
    print([value for value in list1])
    print(list1.get(2))
