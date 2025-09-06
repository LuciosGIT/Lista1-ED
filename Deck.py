# Questão 8

from Node import Node

class Deck:

    def __init__ (self):
        self.head = None
        self.size = 0


    def insertOnHead(self, data) -> None:
        
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            self.head.prev = None
            self.size += 1

        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.size += 1

    def insertOnTail(self, data) -> None:

        newNode = Node(data)

        if not self.head:
            self.head = newNode
            self.head.prev = None
            self.size += 1
        
        else: 
            pointer = self.head

            while pointer.next:       
                pointer = pointer.next
            pointer.next = newNode
            newNode.prev = pointer
            self.size += 1
    
    def removeFromHead(self) -> None:

        if not self.head:
            raise Exception('A lista está vazia!')
        
        if self.size == 1:
            self.head = None
            self.size -= 1
            return

        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
    

    def removeFromTail(self) -> None:

        if not self.head:
            raise Exception('A lista está vazia!')
        
        if self.size == 1:
            self.head = None
            self.size -= 1
            return

        pointer = self.head
        while pointer.next:
            pointer = pointer.next
        pointer.prev.next = None
        self.size -= 1

    def peek(self):
        elements = []
        pointer = self.head
        while pointer:
            elements.append(pointer.data)
            pointer = pointer.next
        return elements
    


dll = Deck()
dll.insertOnHead(10)
dll.insertOnTail(20)
dll.insertOnTail(30)
dll.removeFromHead()
dll.removeFromTail()

print(dll.peek()) 


        
                
