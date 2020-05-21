class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_Empty():
            return self.stack.pop()

    def is_Empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_Empty():
            return self.stack[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if not self.is_Empty():
            return self.items.pop()

    def is_Empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_Empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeTraversal:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder(self.root)
        elif traversal_type == "reverselevelorder":
            return self.reverselevelorder(self.root)
        else:
            print("Invalid traversal type!")
            return False

    def preorder(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal) 
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal +=  str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        
        return traversal

    def reverselevelorder(self, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while not stack.is_Empty():
            traversal += str(stack.pop().value) + "-"
        return traversal

tree = BinaryTreeTraversal(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverselevelorder"))