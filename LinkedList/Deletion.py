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

    def delete_node(self, key):
        curr_node = self.head
        # Case 1: Node to be deleted is head node
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        # Case 2: Node to be deleted is any other node
        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = prev_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None

    def delete_node_at_pos(self,pos): 
        curr_node = self.head
        # Case 1: Node to be deleted is head node
        if pos == 0:
            self.head = curr_node.next
            curr_node = None
            return
        # Case 2: Node to be deleted is any other node
        prev_node = None
        count = 0
        while curr_node and count!=pos:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None

ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
# ll.print_list()
ll.delete_node("C")
# ll.print_list()
ll.delete_node_at_pos(1)
ll.print_list()