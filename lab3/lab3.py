class SinglyLinkedList:
    
    class Node:
        item = None
        next_node = None

        def __init__(self, item, next_node = None):
            self.item = item
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.len = 0
    
    def add(self, item):
        if not self.head:
            self.head = self.Node(item)
            self.len += 1
            return
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(item)
        self.len += 1

    def insert(self, item, index):              
        if index == 0:
            self.head = self.Node(item, self.head)
            return

        i = 0
        node = self.head
        p_node = self.head

        while i < index:
            p_node = node
            node = node.next_node
            i += 1
        p_node.next_node = self.Node(item, next_node=node)
        self.len += 1

    def get(self, index):
        i = 0
        node = self.head

        while i < index:
            node = node.next_node
            i += 1

        return node.item

    def delete(self, index):
        if index == 0:
            self.head = self.head.next_node
        
        i = 0
        node = self.head
        p_node = self.head
        
        while i < index:
            p_node = node
            node = node.next_node
            i += 1

        p_node.next_node = node.next_node
        item = node.item

        del node
        
        self.len -= 1

        return item
        

    def print(self):
        node = self.head
        
        while node.next_node:
            print(node.item)
            node = node.next_node
        print(node.item)


 
linked_list = SinglyLinkedList()

linked_list.add(823)
linked_list.add("www")
linked_list.add(3.3)
linked_list.add(True)

linked_list.insert(555, 0)

linked_list.print()

print(linked_list.len)
linked_list.delete(0)
print(linked_list.len)
