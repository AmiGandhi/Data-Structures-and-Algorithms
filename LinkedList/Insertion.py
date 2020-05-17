class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, data):
        new_node = Node(data)
        # Case 1: No element in the LinkedList
        if self.head is None:
            self.head = new_node
            return
        #Case 2: Elements present in LinkedList
        curr_Node = self.head
        while curr_Node.next:
            curr_Node = curr_Node.next
        curr_Node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        # Case 1: No element in the LinkedList
        if self.head is None:
            self.head = new_node
            return
        # Case 2: Elements present in LinkedList
        curr_node = self.head
        new_node.next = curr_node
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        #Case 1: Node not present
        if not prev_node:
            return
        # Case 2: If node is present
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


ll = LinkedList()
ll.append("B")
ll.append("C")
# ll.print_list()
ll.prepend("A")
# ll.print_list()
ll.insert_after_node(ll.head.next, "D")
ll.print_list()