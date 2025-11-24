class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        # self.pref = None
# {'item': data, nref: None, pref: None}


class LinkedList:

    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        # self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        # new_node.pref = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                # new_node.pref = n
                new_node.nref = n.nref
                # if n.nref is not None:
                # n.nref.prev = new_node
                n.nref = new_node

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref

    def element_in_list(self, x):
        if self.start_node is None:
            print('False')
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print('True')
                return
            if n.nref is not None:
                n = n.nref
            else:
                n = None
        print('False')
        return

    def ai_an(self, i):
        j = 0
        n = self.start_node
        while n is not None:
            if j >= i:
                print(n.item)
            j += 1
            if n.nref is not None:
                n = n.nref
            else:
                n = None


new_linked_list = LinkedList()
new_linked_list.insert_in_emptylist(50)
new_linked_list.insert_at_start(10)
new_linked_list.insert_at_start(5)
new_linked_list.insert_at_start(18)
new_linked_list.traverse_list()
new_linked_list.element_in_list(50)
new_linked_list.element_in_list(10)
new_linked_list.element_in_list(5)
new_linked_list.element_in_list(18)
new_linked_list.element_in_list(69)
new_linked_list.ai_an(2)
