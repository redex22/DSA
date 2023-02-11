class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head) if head is not None else None
        self.tail = self.head
        self.length = 1 if head is not None else 0

    def append(self, value):
        """Inserts a value as the last node of the Linked List
        :param value: value to be inserted of any type"""
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
            self.tail = current_node.next
            self.length += 1

    def preappend(self, value):
        """Insert a new node as the head of the Linked List
        :param value: value to be inserted of any type"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get(self, index: int):
        """If the position exists, returns the value of that given position.
        Otherwise, raise an IndexError
        :param index: position of the value you want to get
        :return: value at the given position"""
        curr_idx = 0
        current_node = self.head
        while current_node:
            if curr_idx == index:
                return current_node.value
            curr_idx += 1
            current_node = current_node.next
        raise IndexError("Value out of range")

    def __len__(self):
        return self.length

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
    print(list2.tail.value)
    list2.append("Dos")
    list2.append("Tres")
    print(list2.tail.value)
    print(list1) # int linked list: 1 -> 2 -> 3
    print(list2) # str linked list: Uno -> Dos -> Tres
    print(f"Length of list1: {len(list1)}\nLength of list2: {len(list2)}")  # Length of list1: 3
                                                                            # Length of list2: 3
    print([value for value in list1]) # [1, 2, 3]
    print(list1.get(2)) # 3
    try:
        list1.get(5)
    except IndexError as ie:
        print(f"Houston we had a problem: {ie}") # IndexError shows up as expected ("Value out of range")

    list3 = LinkedList(5)
    list3.preappend(1)
    print(list3)
    print(list3.tail)
    print(list3.head)
    print(len(list3))
